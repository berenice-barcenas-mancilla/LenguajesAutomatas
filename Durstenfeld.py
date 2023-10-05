import tkinter as tk
from tkinter import simpledialog, messagebox

# Función para imprimir el itinerario a partir de una fuente dada src
def print_itinerary(trayectos, src):
    # Obtenemos el destino correspondiente a la fuente
    dest = trayectos.get(src)
    # Si no hay destino, terminamos
    if not dest:
        return

    # Agregamos el itinerario a la variable de resultados
    result.append(src + ' —> ' + dest)
    # Llamamos a la función recursivamente con el destino como nueva fuente
    print_itinerary(trayectos, dest)

# Función para encontrar el itinerario a partir de una lista dada de aeropuertos de salida y llegada
def findItinerary(trayectos):
    # Construimos un conjunto de aeropuertos de destino
    destinos = {*trayectos.values()}

    # Consideramos cada aeropuerto de salida para encontrar el aeropuerto de origen
    for k, v in trayectos.items():
        # El aeropuerto de origen no estará presente en la lista de aeropuertos de destino
        if k not in destinos:
            # Cuando encontramos el aeropuerto de origen, imprimimos el itinerario
            print_itinerary(trayectos, k)
            return

# Función para solicitar el número de trayectos al usuario y obtener los trayectos
def get_user_input():
    num_trayectos = simpledialog.askinteger("Número de Trayectos", "¿Cuántos trayectos vas a recorrer?")
    if num_trayectos:
        trayectos = {}
        for i in range(num_trayectos):
            origen = simpledialog.askstring("Origen", f"Ingrese el origen del trayecto {i + 1}")
            destino = simpledialog.askstring("Destino", f"Ingrese el destino del trayecto {i + 1}")
            trayectos[origen] = destino
        return trayectos
    else:
        return None

if __name__ == '__main__':
    # Crear una ventana Tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Variable para almacenar el resultado
    result = []

    # Solicitar los trayectos al usuario
    user_tickets = get_user_input()

    if user_tickets:
        # Llamamos a la función para encontrar el itinerario
        findItinerary(user_tickets)

        # Mostrar el resultado en una ventana emergente
        result_text = "\n".join(result)
        messagebox.showinfo("Itinerario", f"Camino Mínimo:\n{result_text}")

    # Cerrar la ventana principal de Tkinter
    root.destroy()
