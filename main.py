import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk 
import matplotlib

matplotlib.use('Agg')

def graficar_onda(amplitud, frecuencia, velocidad):
    # Calcular la longitud de onda     
    longitud_de_onda = velocidad / frecuencia

    # Crear un espacio de tiempo
    x = np.linspace(0, 2 * longitud_de_onda, 1000)

    # Función de onda sinusoidal
    y = amplitud * np.sin(2 * np.pi * x / longitud_de_onda)
   
    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y, label='Onda sinusoidal')
    ax.axvline(x=longitud_de_onda, color='r', linestyle='--', label='Longitud de onda (λ)')
    ax.axvline(x=2 * longitud_de_onda, color='r', linestyle='--')
    ax.axhline(y=amplitud, color='g', linestyle='--', label='Amplitud (+A)')
    ax.axhline(y=-amplitud, color='g', linestyle='--', label='Amplitud (-A)')

    # Etiquetas y leyenda
    ax.set_title('La longitud de onda es de λ = {:.2f} m'.format(longitud_de_onda))
    ax.set_xlabel('Distancia (m)')
    ax.set_ylabel('Amplitud')
    ax.legend()
    ax.grid(True)

    # Mostrar la figura en tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
def calcular_y_graficar():
    try:
        frecuencia = float(entry_frecuencia.get())
        velocidad = float(entry_velocidad.get())
        amplitud = float(entry_amplitud.get())
        graficar_onda(amplitud, frecuencia, velocidad)
    except ValueError:
        label_resultado.config(text="Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora Gráfica de Longitud de Onda")

# Crear y ubicar los widgets en la ventana
tk.Label(window, text="Frecuencia (Hz):").pack()
entry_frecuencia = tk.Entry(window)
entry_frecuencia.pack()

tk.Label(window, text="Velocidad (m/s):").pack()
entry_velocidad = tk.Entry(window)
entry_velocidad.pack()

tk.Label(window, text="Amplitud:").pack()
entry_amplitud = tk.Entry(window)
entry_amplitud.pack()

tk.Button(window, text="Calcular y Graficar", command=calcular_y_graficar).pack(pady=10)

label_resultado = tk.Label(window, text="")
label_resultado.pack()

# Ejecutar la pequeña aplicación de tkinter
window.mainloop()
