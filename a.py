    import tkinter as tk
    from tkhtmlview import HTMLLabel
    
    root = tk.Tk()
    root.title("Embedded Website")
    
    html_label = HTMLLabel(root, width=800, height=600)
    html_label.pack(fill="both", expand=True)
    
    # Load the website
    url = "https://www.example.com"
    html_label.load_url(url)
    
    root.mainloop()
