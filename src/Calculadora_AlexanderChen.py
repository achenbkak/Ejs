import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculadora con Tkinter")
root.geometry("600x800")
root.resizable(False, False)

# --- CABECERA ---
frame_cabecera = tk.Frame(root, width=600, height=80)
frame_cabecera.pack(side="top", fill="x", padx=10, pady=10)
frame_cabecera.pack_propagate(False)

# Selector de modo
frameDesplegable = tk.Frame(frame_cabecera, width=150, height=60)
frameDesplegable.pack(side="left", anchor="c", padx=5)
frameDesplegable.pack_propagate(False)

options = ["Estándar", "Científica"]
panel_desplegable = tk.StringVar(value=options[0])

combobox = ttk.Combobox(
    frameDesplegable, 
    textvariable=panel_desplegable, 
    values=options, 
    state="readonly",
    width=12
)
combobox.pack(pady=15)

# Pantalla de resultados
pantalla = tk.Frame(frame_cabecera, width=415, height=60)
pantalla.pack(side="right", fill="both", expand=True, padx=5)
pantalla.pack_propagate(False)

texto = tk.Label(
    pantalla, 
    text="0", 
    bg="black", 
    fg="white", 
    font=("Arial", 28), 
    anchor="e",
    padx=10
)
texto.pack(fill="both", expand=True)

# --- PANEL DE BOTONES ---
zona_botones = tk.Frame(root, width=560, height=620)
zona_botones.pack(side="top", pady=10, padx=20)
zona_botones.pack_propagate(False)

# Rejilla numérica (4 filas x 3 columnas)
botones = tk.Frame(zona_botones, width=400, height=600)
botones.pack(side="left", fill="both", expand=True)

for columna in range(3):
    botones.columnconfigure(columna, weight=1)
for fila in range(4):
    botones.rowconfigure(fila, weight=1)

buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0", ".", "C"
]

for i, button in enumerate(buttons):
    fila = i // 3
    columna = i % 3
    
    boton = tk.Button(
        botones,
        text=button,
        font=("Arial", 24, "bold"),
        bg="#FFA500",
        fg="white",
        activebackground="#FF8C00",
        activeforeground="white",
        bd=0
    )
    boton.grid(row=fila, column=columna, padx=4, pady=4, sticky="nsew")

# Panel de operadores
operaciones = tk.Frame(zona_botones, width=140, height=600)
operaciones.pack(side="right", fill="both", padx=(10, 0))

operaciones.columnconfigure(0, weight=1)
for fila in range(5):
    operaciones.rowconfigure(fila, weight=1)

operadores = ["+", "-", "×", "÷", "="]

for fila, operador in enumerate(operadores):
    boton = tk.Button(
        operaciones,
        text=operador,
        font=("Arial", 22, "bold"),
        bg="#F48473",
        fg="white",
        activebackground="#E06C5B",
        activeforeground="white",
        bd=0
    )
    boton.grid(row=fila, column=0, padx=4, pady=4, sticky="nsew")

# --- PIE DE PÁGINA ---
contenedor = tk.Frame(root, width=600, height=60)
contenedor.pack(side="bottom", fill="x")
contenedor.pack_propagate(False)

texto2 = tk.Label(contenedor, text="Calculadora Tk by DAM II", font=("Arial", 25, "bold"), fg="black")
texto2.pack(expand=True)

root.mainloop()