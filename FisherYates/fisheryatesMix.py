from random import randrange
import tkinter as tk
from tkinter import simpledialog, messagebox

# Función para intercambiar elementos a[i] y a[j] en una lista
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Función para barajar una lista A
def shuffle(A):
    # Lista de lectura desde el índice más abajo hasta el más alto
    for i in range(len(A)):
        # Genera un número aleatorio j tal que i <= j < n
        j = randrange(i, len(A))
        # Realiza un intercambio del elemento actual con el índice generado aleatoriamente
        swap(A, i, j)

if __name__ == '__main__':
    # Pregunta al usuario cuántos datos quiere ingresar
    num_datos = simpledialog.askinteger("Ingresar Datos", "Cuántos datos quieres ingresar?")
    
    if num_datos is not None:
        # Solicita los datos al usuario
        data = []
        for _ in range(num_datos):
            dato = simpledialog.askstring("Ingresar Dato", "Ingresa un dato:")
            data.append(dato)

        # Baraja los datos ingresados
        shuffle(data)

        # Muestra los datos ingresados en una ventana emergente
        data_str = "\n".join(map(str, data))
        messagebox.showinfo("Datos Ingresados", "Los datos ingresados son:\n\n" + data_str)

        # Baraja la lista de datos
        shuffle(data)

        # Muestra el resultado en una ventana emergente
        result_str = "\n".join(map(str, data))
        messagebox.showinfo("Resultado", "El resultado después de barajar es:\n\n" + result_str)
