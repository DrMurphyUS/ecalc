import tkinter as tk
from tkinter import messagebox
import os

# Constantes
HISTORIAL_ARCHIVO = 'historial.txt'

# Operaciones matemáticas con type hints
def sumar(a: float, b: float) -> float: return a + b
def restar(a: float, b: float) -> float: return a - b
def multiplicar(a: float, b: float) -> float: return a * b
def dividir(a: float, b: float):
    return 'No se puede dividir entre cero' if b == 0 else a / b
def potencia(a: float, b: float) -> float: return a ** b
def raiz_cuadrada(a: float):
    return 'Raíz no válida' if a < 0 else a ** 0.5
def modulo(a: float, b: float) -> float: return a % b
def inverso(a: float):
    return 'Inverso indefinido' if a == 0 else 1 / a
def valor_absoluto(a: float) -> float: return abs(a)

# Diccionario de operaciones
OPERACIONES = {
    'sumar': (sumar, "{a} + {b} = {r}"),
    'restar': (restar, "{a} - {b} = {r}"),
    'multiplicar': (multiplicar, "{a} × {b} = {r}"),
    'dividir': (dividir, "{a} ÷ {b} = {r}"),
    'potencia': (potencia, "{a} ^ {b} = {r}"),
    'raiz': (raiz_cuadrada, "√{a} = {r}"),
    'modulo': (modulo, "{a} % {b} = {r}"),
    'inverso': (inverso, "1 / {a} = {r}"),
    'absoluto': (valor_absoluto, "|{a}| = {r}")
}

# Guardar historial
def guardar_historial(operacion: str):
    with open(HISTORIAL_ARCHIVO, 'a') as f:
        f.write(operacion + '\n')

# Cargar historial
def cargar_historial():
    if os.path.exists(HISTORIAL_ARCHIVO):
        with open(HISTORIAL_ARCHIVO, 'r') as f:
            for linea in f:
                historial.insert(tk.END, linea.strip())
    else:
        historial.insert(tk.END, "No hay historial disponible.")

# Borrar historial
def borrar_historial():
    historial.delete(0, tk.END)
    if os.path.exists(HISTORIAL_ARCHIVO):
        os.remove(HISTORIAL_ARCHIVO)

# Copiar resultado
def copiar_resultado():
    resultado = resultado_label.cget("text").replace("Resultado: ", "")
    if resultado and not resultado.startswith("Resultado"):
        root.clipboard_clear()
        root.clipboard_append(resultado)
        messagebox.showinfo("Copiado", "Resultado copiado al portapapeles.")
    else:
        messagebox.showwarning("Atención", "No hay resultado para copiar.")

# Actualizar campo de entrada
def actualizar_entrada(op: str):
    if op in ['raiz', 'inverso', 'absoluto']:
        entry2.config(state='disabled')
        entry2.delete(0, tk.END)
    else:
        entry2.config(state='normal')

# Calcular resultado
def calcular(op: str):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else None

        funcion, plantilla = OPERACIONES[op]

        if op in ['raiz', 'inverso', 'absoluto']:
            resultado = funcion(num1)
            operacion_str = plantilla.format(a=num1, r=resultado)
        else:
            resultado = funcion(num1, num2)
            operacion_str = plantilla.format(a=num1, b=num2, r=resultado)

        resultado_label.config(text=f"Resultado: {resultado}")
        historial.insert(tk.END, operacion_str)
        guardar_historial(operacion_str)

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos.")

# Limpiar campos
def limpiar():
    entry1.delete(0, tk.END)
    entry2.config(state='normal')
    entry2.delete(0, tk.END)
    resultado_label.config(text="Resultado:")

# UI
root = tk.Tk()
root.title("Calculadora Avanzada")
root.geometry("480x550")

tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Botones operaciones
for i, op in enumerate(OPERACIONES):
    tk.Button(
        root,
        text=op.capitalize(),
        command=lambda op=op: [actualizar_entrada(op), calcular(op)]
    ).grid(row=2 + i // 3, column=i % 3, padx=5, pady=5)

# Botones extra
tk.Button(root, text="Limpiar", command=limpiar).grid(row=6, column=1, pady=5)
tk.Button(root, text="Copiar Resultado", command=copiar_resultado).grid(row=7, column=1, pady=5)
tk.Button(root, text="Borrar Historial", command=borrar_historial).grid(row=8, column=1, pady=5)

# Resultado
resultado_label = tk.Label(root, text="Resultado:")
resultado_label.grid(row=9, column=0, columnspan=3, pady=10)

# Historial
frame_historial = tk.Frame(root)
frame_historial.grid(row=10, column=0, columnspan=3, padx=10, pady=5)
scrollbar = tk.Scrollbar(frame_historial)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
historial = tk.Listbox(frame_historial, height=7, yscrollcommand=scrollbar.set, width=60)
historial.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=historial.yview)

# Cargar historial
cargar_historial()

root.mainloop()
