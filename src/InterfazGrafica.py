import tkinter as tk

root = tk.Tk()
root.title("DEMO")
root.geometry("280x80")

hello = tk.Label(root, text="Hola, mundo!", font=("Arial", 24)) 
hello.pack(pady=20)

root.mainloop()