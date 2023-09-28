import random
import tkinter as tk
from tkinter import messagebox

# Función para mezclar la baraja usando el algoritmo de Fisher-Yates
def mezclar_baraja():
    # Crear una baraja de cartas con todas las combinaciones de valor y palo
    baraja = [(valor, palo) for valor in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for palo in ['♥', '♦', '♣', '♠']]
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

    # Mostrar las manos de los jugadores en ventanas emergentes
    for i, mano in enumerate(manos):
        messagebox.showinfo(f"Jugador {i + 1}", f"Cartas del Jugador {i + 1}:\n{', '.join([f'{valor}  {palo}' for valor, palo in mano])}")

    # Mostrar las cartas restantes en la baraja
    for carta in baraja:
        messagebox.showinfo("Carta restante", f"Carta restante: {carta[0]} {carta[1]}")

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
