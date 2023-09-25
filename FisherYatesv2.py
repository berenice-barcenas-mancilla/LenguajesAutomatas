import tkinter as tk  # Importa la biblioteca Tkinter para la interfaz gráfica
from tkinter import simpledialog  # Importa el módulo simpledialog para crear un cuadro de diálogo
from random import randrange  # Importa la función randrange para generar números aleatorios

# Función para intercambiar elementos a[i] y a[j] en una lista
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Función para barajar una lista A
def shuffle(A):
    for i in range(len(A)):
        j = randrange(i, len(A))  # Genera un índice aleatorio j desde i hasta el final de la lista
        swap(A, i, j)  # Intercambia el elemento en la posición i con el elemento en la posición j

def main():
    root = tk.Tk()  # Crea una ventana principal
    root.title("Algoritmo de Fisher Yates")  # Establece el título de la ventana
    
    num_elements = simpledialog.askinteger("Cantidad de Datos", "Ingrese la cantidad de datos que desea:")  # Muestra un cuadro de diálogo para que el usuario ingrese la cantidad de datos
    
    if num_elements is not None:  # Verifica si el usuario ingresó un valor válido
        data = []  # Inicializa una lista vacía para almacenar los datos
        
        label = tk.Label(root, text=f"Cantidad de Datos: {num_elements}")  # Crea una etiqueta para mostrar la cantidad de datos ingresada
        label.pack()  # Agrega la etiqueta a la ventana
        
        for i in range(num_elements):
            entry = tk.Entry(root)  # Crea una entrada de texto para que el usuario ingrese un dato
            entry.pack()  # Agrega la entrada a la ventana
            data.append(entry)  # Agrega la entrada a la lista de datos
        
        def shuffle_and_print():
            user_data = [int(entry.get()) for entry in data]  # Obtiene los datos ingresados por el usuario y los convierte en una lista de enteros
            shuffle(user_data)  # Baraja la lista de datos
            result_label.config(text=f"Lista barajada: {user_data}")  # Actualiza la etiqueta de resultados con la lista barajada
        
        shuffle_button = tk.Button(root, text="Barajar", command=shuffle_and_print)  # Crea un botón que llama a la función shuffle_and_print cuando se hace clic
        shuffle_button.pack()  # Agrega el botón a la ventana
        
        result_label = tk.Label(root, text="")  # Crea una etiqueta vacía para mostrar los resultados
        result_label.pack()  # Agrega la etiqueta de resultados a la ventana
        
        root.mainloop()  # Inicia el bucle principal de la interfaz gráfica

if __name__ == '__main__':
    main()  # Llama a la función main cuando se ejecuta el programa
