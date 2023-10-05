import tkinter as tk
from tkinter import simpledialog

def findMajorityElement(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    return -1

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # Preguntar al usuario cuántos datos quiere ingresar
    num_data = simpledialog.askinteger("Ingresar datos", "Cuantos datos quieres ingresar?")

    # Validar que num_data sea un número positivo
    if num_data is not None and num_data > 0:
        # Solicitar al usuario que ingrese los datos
        nums = []
        for i in range(num_data):
            while True:
                try:
                    num = simpledialog.askinteger("Ingresar dato", f"Ingrese el dato #{i + 1}:")
                    if num is not None:
                        nums.append(num)
                        break
                except ValueError:
                    pass

        # Mostrar los datos ingresados en una ventana emergente
        data_str = ', '.join(map(str, nums))
        tk.messagebox.showinfo("Datos ingresados", f"Los datos ingresados son: {data_str}")

        # Encontrar el elemento mayoritario
        result = findMajorityElement(nums)
        if result != -1:
            tk.messagebox.showinfo("Resultado", f"El elemento mayoritario es {result}")
        else:
            tk.messagebox.showinfo("Resultado", "El elemento mayoritario no existe")
    else:
        tk.messagebox.showerror("Error", "Debes ingresar un número válido y positivo de datos.")

    root.mainloop()
