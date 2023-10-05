import tkinter as tk
from tkinter import simpledialog, messagebox

def findMajorityElement(nums):
    d = {}
    
    for i in nums:
        d[i] = d.get(i, 0) + 1
    
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    
    return -1

def get_user_input():
    try:
        num_data = simpledialog.askinteger("Ingresar Datos", "¿Cuántos datos desea ingresar?")
        if num_data is not None:
            data = []
            for _ in range(num_data):
                user_input = simpledialog.askstring("Ingresar Datos", "Ingrese un dato (letras solamente):")
                if user_input is not None and user_input.isalpha():
                    data.append(user_input)
                else:
                    messagebox.showerror("Error", "Ingrese letras válidas.")
                    return

            result = findMajorityElement(data)
            show_result(data, result)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para la cantidad de datos.")

def show_result(data, result):
    if result != -1:
        data_str = ', '.join(data)
        messagebox.showinfo("Datos ingresados", f"Datos ingresados: {data_str}\nEl elemento mayoritario es: {result}")
    else:
        messagebox.showinfo("Resultado", "El elemento mayoritario no existe")

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    get_user_input()
    root.mainloop()
