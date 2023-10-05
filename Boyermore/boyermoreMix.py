import tkinter as tk
from tkinter import simpledialog

def findMajorityElement(data):
    d = {}
    for item in data:
        d[item] = d.get(item, 0) + 1

    for key, value in d.items():
        if value > len(data) / 2:
            return key
    return -1

def main():
    # Pedir al usuario cuántos datos desea ingresar
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    num_data = simpledialog.askinteger("Número de datos", "¿Cuántos datos desea ingresar?")

    if num_data is not None:
        data = []
        for i in range(num_data):
            # Pedir al usuario que ingrese un dato
            data_entry = simpledialog.askstring(f"Dato {i+1}", f"Ingrese el dato {i+1} (número o letra):")
            data.append(data_entry)

        # Calcular el elemento mayoritario
        result = findMajorityElement(data)

        # Mostrar los datos ingresados y el resultado en ventanas emergentes
        tk.messagebox.showinfo("Datos ingresados", f"Datos ingresados por el usuario: {', '.join(data)}")

        if result != -1:
            tk.messagebox.showinfo("Resultado", f"El elemento mayoritario es: {result}")
        else:
            tk.messagebox.showinfo("Resultado", "El elemento mayoritario no existe")

if __name__ == '__main__':
    main()
