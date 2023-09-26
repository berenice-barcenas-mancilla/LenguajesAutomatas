import random
import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter import messagebox

# Función para intercambiar elementos a[i] y a[j] en una lista
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Función para barajar una lista A
def shuffle(A):
    # Lista de lectura desde el índice más bajo hasta el más alto
    for i in range(len(A)):
        # Genera un número aleatorio j tal que i <= j < n
        j = random.randrange(i, len(A))
        # Realiza un intercambio del elemento actual con el índice generado aleatoriamente
        swap(A, i, j)

if __name__ == '__main__':
    # Pedir al usuario cuántos datos quiere ingresar
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    num_data = askinteger("Ingresar datos", "Cuantos datos desea ingresar:")  # Pregunta al usuario cuántos datos desea ingresar

    if num_data is not None:
        data = []  # Lista para almacenar los datos ingresados por el usuario

        for _ in range(num_data):
            # Pedir al usuario un dato utilizando una ventana emergente
            dato = askinteger("Ingresar dato", "Ingrese un dato:")  # Pide al usuario un dato y lo guarda en 'dato'
            if dato is not None:
                data.append(dato)  # Agrega el dato a la lista 'data'

        if data:
            shuffle(data)  # Barajar los datos ingresados por el usuario

            # Crear una ventana emergente para mostrar la lista barajada
            result_window = tk.Tk()
            result_window.title("Lista Barajada")  # Establece el título de la ventana emergente
            
            # Crear una etiqueta para mostrar la lista barajada
            result_label = tk.Label(result_window, text=str(data))  # Crea una etiqueta con la lista barajada
            result_label.pack(padx=20, pady=20)  # Añade la etiqueta a la ventana con relleno
            
            result_window.mainloop()  # Muestra la ventana emergente y espera a que el usuario la cierre
