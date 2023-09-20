
import tkinter as tk
from tkinter import simpledialog, messagebox

def findMajorityElement(nums):
    # Crea un hash map vacío
    d = {}
    
    # Almacena la frecuencia de datos de cada elemento en un diccionario
    for i in nums:
        d[i] = d.get(i, 0) + 1
    
    # Busca el elemento mayoritario
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    
    # NINGÚN ELEMENTO MAYORITARIO ESTÁ PRESENTE
    return -1
    
def main():
    # Crea una ventana principal
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    try:
        # Solicita al usuario la cantidad de datos que desea ingresar
        num_data = simpledialog.askinteger("Cantidad de Datos", "Ingrese la cantidad de datos:")

        # Solicita al usuario ingresar los datos separados por comas
        input_data = simpledialog.askstring("Datos", f'Ingrese {num_data} datos separados por comas:')
        
        # Convierte los datos ingresados en una lista de enteros
        nums = [int(x) for x in input_data.split(',')]

        # Verifica si el elemento mayoritario existe
        result = findMajorityElement(nums)
        if result != -1:
            messagebox.showinfo("Resultado", f'El elemento mayoritario es {result}')
        else:
            messagebox.showinfo("Resultado", "El elemento mayoritario no existe")

    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válida de datos o datos válidos separados por comas.")

    root.mainloop()

if __name__ == '__main__':
    main()
