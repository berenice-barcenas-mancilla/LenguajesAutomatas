import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Función para barajar una lista A
def shuffle(A):
    for i in range(len(A)):
        j = random.randrange(i, len(A))
        A[i], A[j] = A[j], A[i]

if __name__ == '__main__':
    # Crear una ventana principal (opcional)
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    try:
        # Pedir al usuario cuántos datos quiere ingresar
        num_datos = simpledialog.askinteger("Ingresar Datos", "Cuántos datos desea ingresar?")

        if num_datos is not None:
            datos = []
            for i in range(num_datos):
                # Pedir al usuario ingresar un dato (letra)
                dato = simpledialog.askstring("Ingresar Dato", f"Ingrese el dato #{i + 1} (solo letras):")
                if dato is not None and dato.isalpha():
                    datos.append(dato)
                else:
                    messagebox.showerror("Error", "Ingrese solo letras.")
                    
            # Mostrar los datos ingresados en una ventana emergente
            messagebox.showinfo("Datos Ingresados", "Datos ingresados: " + ', '.join(datos))

            # Barajar los datos
            shuffle(datos)


            # Mostrar el resultado (datos barajados) en una ventana emergente
            messagebox.showinfo("Resultado", "Datos barajados: " + ', '.join(datos))

    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Cerrar la ventana principal (opcional)
    root.destroy()
