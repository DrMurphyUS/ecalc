import tkinter as tk from tkinter import messagebox

Funciones de operaciones

def sumar(a, b): return a + b

def restar(a, b): return a - b

def multiplicar(a, b): return a * b

def dividir(a, b): if b == 0: return "No se puede dividir entre cero" return a / b

Función para realizar la operación

def calcular(operacion): try: num1 = float(entry1.get()) num2 = float(entry2.get()) if operacion == 'sumar': resultado = sumar(num1, num2) elif operacion == 'restar': resultado = restar(num1, num2) elif operacion == 'multiplicar': resultado = multiplicar(num1, num2) elif operacion == 'dividir': resultado = dividir(num1, num2) resultado_label.config(text=f"Resultado: {resultado}") except ValueError: messagebox.showerror("Error", "Por favor ingresa números válidos.")

Configuración de la ventana principal

root = tk.Tk() root.title("Calculadora GUI") root.geometry("300x300")

Etiquetas y campos de entrada

tk.Label(root, text="Número 1:").pack() entry1 = tk.Entry(root) entry1.pack()

tk.Label(root, text="Número 2:").pack() entry2 = tk.Entry(root) entry2.pack()

Botones para cada operación

tk.Button(root, text="Sumar", command=lambda: calcular('sumar')).pack() tk.Button(root, text="Restar", command=lambda: calcular('restar')).pack() tk.Button(root, text="Multiplicar", command=lambda: calcular('multiplicar')).pack() tk.Button(root, text="Dividir", command=lambda: calcular('dividir')).pack()

Etiqueta para mostrar el resultado

resultado_label = tk.Label(root, text="Resultado:") resultado_label.pack()

Ejecutar la aplicación

root.mainloop()

