import tkinter as tk
root = tk.Tk()
root.title("Calculadora con TKinter")
root.geometry("600x800")

pantalla = tk.Frame(root, width=600, height=100)
pantalla.pack()
pantalla.pack_propagate(False)

texto = tk.Label(
    pantalla, 
    text="0",
    width=50,
    height=3,
    bg="black",
    fg="white",
    font= ("Arial", 30),
    anchor="e")
texto.pack(side="top", padx=20, pady=10)

zona_botones = tk.Frame(root)
zona_botones.pack(fill="both", expand=True, padx=20, pady=10)

botones = tk.Frame(zona_botones,height=500)
botones.pack(side="left", fill="both",expand=True)
botones.pack_propagate(False)
# Hacemos que las 3 columnas tengan el mismo tamaño
for columna in range(3):
    botones.columnconfigure(columna, minsize=135)

for fila in range(4):
    botones.rowconfigure(fila, minsize=145)
buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

for i, button in enumerate(buttons):
    fila = i // 3
    columna = i % 3
  
    boton = tk.Button(
        botones,
        text=button,
        font=("Arial",50),
        bg="orange",
        fg="white"
        
    )

    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

operaciones = tk.Frame(zona_botones, width=150,height=500)
operaciones.pack(side="left", fill="y")
operaciones.pack_propagate(False)

for fila in range(5):
    operaciones.rowconfigure(fila, minsize=115)

operaciones.columnconfigure(0, minsize=150)

operadores = ["+", "-", "×", "÷","="]


for fila, operador in enumerate(operadores):

    boton = tk.Button(
        operaciones,
        text=operador,
        font=("Arial", 30),
        bg="#F48473",
        fg="white"
    )

    boton.grid(
        row=fila,
        column=0,
        padx=5,
        pady=5,
        sticky="nsew"
    )

contenedor = tk.Frame(root, width=600, height=200)
contenedor.pack(pady=10)
contenedor.pack_propagate(False)
texto2 = tk.Label(contenedor, text="Calculadora Tk by DAM II", font=("Arial",25))
texto2.pack(side="bottom",pady=15)
root.mainloop()