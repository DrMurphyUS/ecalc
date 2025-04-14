import tkinter as tk
from tkinter import messagebox
import os

# Archivo para guardar el historial
HISTORIAL_ARCHIVO = 'historial.txt'

# Funciones de operaciones
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0:
        return 'No se puede dividir entre cero'
    return a / b
def potencia(a, b): return a ** b
def raiz_cuadrada(a):
    if a < 0:
        return 'Raíz de número negativo no está definida'
    return a ** 0.5
def modulo(a, b): return a % b
def inverso(a):
    if a == 0:
        return 'No existe el inverso de cero'
    return 1 / a
def valor_absoluto(a): return abs(a)

# Guardar historial en archivo
def guardar_historial(operacion):
    with open(HISTORIAL_ARCHIVO, 'a') as file:
        file.write(operacion + '\n')

# Cargar historial del archivo
def cargar_historial():
    if os.path.exists(HISTORIAL_ARCHIVO):
        with open(HISTORIAL_ARCHIVO, 'r') as file:
            for linea in file:
                historial.insert(tk.END, linea.strip())
    else:
        historial.insert(tk.END, "No hay historial disponible.")

# Borrar historial
def borrar_historial():
    historial.delete(0, tk.END)
    if os.path.exists(HISTORIAL_ARCHIVO):
        os.remove(HISTORIAL_ARCHIVO)

# Copiar resultado al portapapeles
def copiar_resultado():
    resultado = resultado_label.cget("text").replace("Resultado: ", "")
    if resultado and not resultado.startswith("Resultado"):
        root.clipboard_clear()
        root.clipboard_append(resultado)
        messagebox.showinfo("Copiado", "Resultado copiado al portapapeles.")
    else:
        messagebox.showwarning("Atención", "No hay un resultado válido para copiar.")

# Actualizar entrada2 según la operación
def actualizar_entrada(op):
    if op in ['raiz', 'inverso', 'absoluto']:
        entry2.config(state='disabled')
        entry2.delete(0, tk.END)
    else:
        entry2.config(state='normal')

# Función para realizar la operación
def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else None

        if operacion == 'sumar':
            resultado = sumar(num1, num2)
            operacion_str = f"{num1} + {num2} = {resultado}"
        elif operacion == 'restar':
            resultado = restar(num1, num2)
            operacion_str = f"{num1} - {num2} = {resultado}"
        elif operacion == 'multiplicar':
            resultado = multiplicar(num1, num2)
            operacion_str = f"{num1} × {num2} = {resultado}"
        elif operacion == 'dividir':
            resultado = dividir(num1, num2)
            operacion_str = f"{num1} ÷ {num2} = {resultado}"
        elif operacion == 'potencia':
            resultado = potencia(num1, num2)
            operacion_str = f"{num1} ^ {num2} = {resultado}"
        elif operacion == 'raiz':
            resultado = raiz_cuadrada(num1)
            operacion_str = f"√{num1} = {resultado}"
        elif operacion == 'modulo':
            resultado = modulo(num1, num2)
            operacion_str = f"{num1} % {num2} = {resultado}"
        elif operacion == 'inverso':
            resultado = inverso(num1)
            operacion_str = f"1 / {num1} = {resultado}"
        elif operacion == 'absoluto':
            resultado = valor_absoluto(num1)
            operacion_str = f"|{num1}| = {resultado}"

        resultado_label.config(text=f"Resultado: {resultado}")
        historial.insert(tk.END, operacion_str)
        guardar_historial(operacion_str)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Función para limpiar campos
def limpiar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry2.config(state='normal')
    resultado_label.config(text="Resultado:")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora Avanzada GUI Mejorada")
root.geometry("480x550")

# Etiquetas y campos de entrada
tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Botones de operaciones
operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Potencia", "Raíz", "Módulo", "Inverso", "Absoluto"]
for i, op in enumerate(operaciones):
    tk.Button(
        root,
        text=op,
        command=lambda op=op.lower(): [actualizar_entrada(op), calcular(op)]
    ).grid(row=2 + i // 3, column=i % 3, padx=5, pady=5)

# Botones adicionales
tk.Button(root, text="Limpiar", command=limpiar).grid(row=5, column=1, pady=10)
tk.Button(root, text="Copiar Resultado", command=copiar_resultado).grid(row=6, column=1, pady=5)
tk.Button(root, text="Borrar Historial", command=borrar_historial).grid(row=7, column=1, pady=5)

# Etiqueta de resultado
resultado_label = tk.Label(root, text="Resultado:")
resultado_label.grid(row=8, column=0, columnspan=3, pady=10)

# Historial de operaciones
frame_historial = tk.Frame(root)
frame_historial.grid(row=9, column=0, columnspan=3, padx=10, pady=5)
scrollbar = tk.Scrollbar(frame_historial)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
historial = tk.Listbox(frame_historial, height=7, yscrollcommand=scrollbar.set, width=60)
historial.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=historial.yview)

# Cargar historial previo
cargar_historial()

# Ejecutar la aplicación
root.mainloop()