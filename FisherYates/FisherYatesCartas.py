import random
import tkinter as tk
from tkinter import messagebox

# Función para mezclar la baraja usando el algoritmo de Fisher-Yates
def mezclar_baraja():
    # Crear una baraja de cartas con todas las combinaciones de valor y palo
    baraja = [(valor, palo) for valor in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for palo in ['corazon', 'diamante', 'trevol', 'pica']]
    random.shuffle(baraja)  # Mezclar la baraja de cartas
    return baraja

# Función para repartir cartas a los jugadores
def repartir_cartas():
    jugadores = int(entrada_jugadores.get())  # Obtener el número de jugadores desde la entrada de texto

    # Verificar si el número de jugadores es válido (al menos dos y menos de 5)
    if jugadores < 2 or jugadores >= 5:
        messagebox.showerror("Error", "El número de jugadores debe ser mayor o igual a 2 y menor que 5.")
        return

    baraja = mezclar_baraja()  # Mezclar la baraja de cartas
    manos = [[] for _ in range(jugadores)]  # Crear una lista vacía para cada jugador

    # Repartir 7 cartas a cada jugador
    for _ in range(7):
        for jugador in manos:
            jugador.append(baraja.pop())  # Tomar una carta de la baraja y agregarla a la mano del jugador

    # Crear una ventana para mostrar las cartas
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados del Reparto de Cartas")
    ventana_resultados.geometry("400x300")  # Establecer el tamaño de la ventana

    # Cuadro de texto para mostrar las manos de los jugadores y las cartas restantes
    texto_resultados = tk.Text(ventana_resultados)
    texto_resultados.pack(fill=tk.BOTH, expand=True)

    # Mostrar las manos de los jugadores en el cuadro de texto
    for i, mano in enumerate(manos):
        mensaje = f"Cartas del Jugador {i + 1}:\n{', '.join([f'{valor} {palo}' for valor, palo in mano])}\n\n"
        texto_resultados.insert(tk.END, mensaje)

    # Mostrar las cartas restantes en la baraja en el cuadro de texto
    mensaje_cartas_restantes = "Cartas restantes en la baraja:\n"
    for carta in baraja:
        mensaje_cartas_restantes += f"{carta[0]} {carta[1]}\n"
    
    texto_resultados.insert(tk.END, mensaje_cartas_restantes)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mezcla y Reparto de Cartas")

# Etiqueta e entrada para el número de jugadores
etiqueta_jugadores = tk.Label(ventana, text="Número de jugadores:")
etiqueta_jugadores.pack()
entrada_jugadores = tk.Entry(ventana)
entrada_jugadores.pack()

# Botón para repartir cartas
boton_repartir = tk.Button(ventana, text="Repartir Cartas", command=repartir_cartas)
boton_repartir.pack()

ventana.mainloop()  # Iniciar el bucle principal de la ventana
