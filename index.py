import tkinter as tk from tkinter import messagebox import os

Archivo para guardar el historial

HISTORIAL_ARCHIVO = 'historial.txt'

Funciones de operaciones

def sumar(a, b): return a + b

def restar(a, b): return a - b

def multiplicar(a, b): return a * b

def dividir(a, b): if b == 0: return 'No se puede dividir entre cero' return a / b

def potencia(a, b): return a ** b

def raiz_cuadrada(a): if a < 0: return 'Raíz de número negativo no está definida' return a ** 0.5

def modulo(a, b): return a % b

Guardar historial en archivo

def guardar_historial(operacion): with open(HISTORIAL_ARCHIVO, 'a') as file: file.write(operacion + '\n')

Cargar historial del archivo

def cargar_historial(): if os.path.exists(HISTORIAL_ARCHIVO): with open(HISTORIAL_ARCHIVO, 'r') as file: for linea in file: historial.insert(tk.END, linea.strip())

Borrar historial

def borrar_historial(): historial.delete(0, tk.END) if os.path.exists(HISTORIAL_ARCHIVO): os.remove(HISTORIAL_ARCHIVO)

Función para realizar la operación

def calcular(operacion): try: num1 = float(entry1.get()) num2 = float(entry2.get()) if entry2.get() else None if operacion == 'sumar': resultado = sumar(num1, num2) elif operacion == 'restar': resultado = restar(num1, num2) elif operacion == 'multiplicar': resultado = multiplicar(num1, num2) elif operacion == 'dividir': resultado = dividir(num1, num2) elif operacion == 'potencia': resultado = potencia(num1, num2) elif operacion == 'raiz': resultado = raiz_cuadrada(num1) elif operacion == 'modulo': resultado = modulo(num1, num2) resultado_label.config(text=f"Resultado: {resultado}") operacion_str = f"{operacion.capitalize()}: {resultado}" historial.insert(tk.END, operacion_str) guardar_historial(operacion_str) except ValueError: messagebox.showerror("Error", "Por favor ingresa números válidos.")

Función para limpiar campos

def limpiar(): entry1.delete(0, tk.END) entry2.delete(0, tk.END) resultado_label.config(text="Resultado:")

Configuración de la ventana principal

root = tk.Tk() root.title("Calculadora Avanzada GUI Mejorada") root.geometry("400x450")

Etiquetas y campos de entrada

tk.Label(root, text="Número 1:").grid(row=0, column=0) entry1 = tk.Entry(root) entry1.grid(row=0, column=1)

tk.Label(root, text="Número 2:").grid(row=1, column=0) entry2 = tk.Entry(root) entry2.grid(row=1, column=1)

Botones para cada operación

operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Potencia", "Raíz", "Módulo"] for i, op in enumerate(operaciones): tk.Button(root, text=op, command=lambda op=op.lower(): calcular(op)).grid(row=2 + i // 3, column=i % 3)

Botón para limpiar campos

tk.Button(root, text="Limpiar", command=limpiar).grid(row=5, column=1)

Botón para borrar historial

tk.Button(root, text="Borrar Historial", command=borrar_historial).grid(row=6, column=1)

Etiqueta para mostrar el resultado

resultado_label = tk.Label(root, text="Resultado:") resultado_label.grid(row=7, column=0, columnspan=3)

Historial de operaciones

historial = tk.Listbox(root, height=5) historial.grid(row=8, column=0, columnspan=3) cargar_historial()

Ejecutar la aplicación

root.mainloop()

