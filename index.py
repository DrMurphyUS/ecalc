import tkinter as tk
from tkinter import messagebox
import os

# -------------------- Constantes --------------------
HISTORIAL_ARCHIVO = 'historial.txt'
DECIMALES = 6

# -------------------- Operaciones --------------------
def sumar(a: float, b: float) -> float: return a + b
def restar(a: float, b: float) -> float: return a - b
def multiplicar(a: float, b: float) -> float: return a * b
def dividir(a: float, b: float): return 'Error: división entre cero' if b == 0 else a / b
def potencia(a: float, b: float) -> float: return a ** b
def raiz_cuadrada(a: float): return 'Error: raíz negativa' if a < 0 else a ** 0.5
def modulo(a: float, b: float) -> float: return a % b
def inverso(a: float): return 'Error: sin inverso' if a == 0 else 1 / a
def valor_absoluto(a: float) -> float: return abs(a)

OPERACIONES = {
    'Sumar': (sumar, "{a} + {b} = {r}"),
    'Restar': (restar, "{a} - {b} = {r}"),
    'Multiplicar': (multiplicar, "{a} × {b} = {r}"),
    'Dividir': (dividir, "{a} ÷ {b} = {r}"),
    'Potencia': (potencia, "{a} ^ {b} = {r}"),
    'Raíz': (raiz_cuadrada, "√{a} = {r}"),
    'Módulo': (modulo, "{a} % {b} = {r}"),
    'Inverso': (inverso, "1 / {a} = {r}"),
    'Absoluto': (valor_absoluto, "|{a}| = {r}")
}

# -------------------- Funciones Auxiliares --------------------
def guardar_historial(linea: str):
    with open(HISTORIAL_ARCHIVO, 'a') as f:
        f.write(linea + '\n')

def cargar_historial():
    if os.path.exists(HISTORIAL_ARCHIVO):
        with open(HISTORIAL_ARCHIVO, 'r') as f:
            for linea in f:
                historial.insert(tk.END, linea.strip())
    else:
        historial.insert(tk.END, "No hay historial.")

def borrar_historial():
    historial.delete(0, tk.END)
    if os.path.exists(HISTORIAL_ARCHIVO):
        os.remove(HISTORIAL_ARCHIVO)

def copiar_resultado():
    resultado = resultado_label.cget("text").replace("Resultado: ", "")
    if resultado and not resultado.startswith("Error"):
        root.clipboard_clear()
        root.clipboard_append(resultado)
        messagebox.showinfo("Copiado", "Resultado copiado al portapapeles.")
    else:
        messagebox.showwarning("Advertencia", "No hay resultado válido para copiar.")

def actualizar_entrada(op: str):
    if op in ['Raíz', 'Inverso', 'Absoluto']:
        entry2.config(state='disabled')
        entry2.delete(0, tk.END)
    else:
        entry2.config(state='normal')

def calcular(op: str):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() and op not in ['Raíz', 'Inverso', 'Absoluto'] else None

        funcion, plantilla = OPERACIONES[op]
        resultado = funcion(num1) if num2 is None else funcion(num1, num2)

        if isinstance(resultado, str):  # es un mensaje de error
            resultado_label.config(text=f"Resultado: {resultado}")
            return

        resultado = round(resultado, DECIMALES)
        operacion_str = plantilla.format(a=num1, b=num2 if num2 is not None else '', r=resultado)

        resultado_label.config(text=f"Resultado: {resultado}")
        historial.insert(tk.END, operacion_str)
        guardar_historial(operacion_str)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def limpiar():
    entry1.delete(0, tk.END)
    entry2.config(state='normal')
    entry2.delete(0, tk.END)
    resultado_label.config(text="Resultado:")

# -------------------- Interfaz --------------------
root = tk.Tk()
root.title("Calculadora Avanzada")
root.geometry("500x600")
root.resizable(False, False)

# Entradas
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Botones de operaciones
for i, op in enumerate(OPERACIONES):
    row = 2 + i // 3
    col = i % 3
    tk.Button(root, text=op, width=14, command=lambda o=op: [actualizar_entrada(o), calcular(o)]).grid(row=row, column=col, padx=5, pady=5)

# Botones extra
tk.Button(root, text="Limpiar", width=16, command=limpiar).grid(row=6, column=0, pady=10)
tk.Button(root, text="Copiar Resultado", width=16, command=copiar_resultado).grid(row=6, column=1, pady=10)
tk.Button(root, text="Borrar Historial", width=16, command=borrar_historial).grid(row=6, column=2, pady=10)

# Resultado
resultado_label = tk.Label(root, text="Resultado:", font=("Arial", 13, 'bold'))
resultado_label.grid(row=7, column=0, columnspan=3, pady=10)

# Historial
frame_historial = tk.Frame(root)
frame_historial.grid(row=8, column=0, columnspan=3, padx=10, pady=5)

scrollbar = tk.Scrollbar(frame_historial)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

historial = tk.Listbox(frame_historial, height=8, width=65, yscrollcommand=scrollbar.set)
historial.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=historial.yview)

# Cargar historial
cargar_historial()

root.mainloop()