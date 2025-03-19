import socket 
import threading
import keyboard
import sys


PORT = 8000
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)

last_msg = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
un = ""

def send(msg):
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (64 - len(send_length))
    client.send(send_length)
    client.send(message)



    

un = input("username: ")
send(un)


def ibx(msg):
    global un
    message = msg.encode("utf-8")
    msg_length = len(message)
    send_length = str(msg_length).encode("utf-8")
    send_length += b' ' * (64 - len(send_length))
    client.send(send_length)
    client.send(message)
    response = client.recv(2048).decode("utf-8") 
    inbox = eval(response)
    for mx in inbox:
        if mx[:len(un)] != un:
            print(mx)


while True:
    act = input("action (message, inbox): ")
    if act == "message":
        inp = input("message: ")
        send(inp)
        if inp == "/bye":
            exit()
    else:
        ibx(";check")