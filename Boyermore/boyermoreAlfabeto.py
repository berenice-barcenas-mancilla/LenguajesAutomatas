import tkinter as tk
from tkinter import simpledialog, messagebox

def findMajorityChar(input_string):
    # Crea un diccionario para almacenar la frecuencia de caracteres
    char_count = {}
    
    # Convierte la cadena de entrada en minúsculas para no distinguir entre mayúsculas y minúsculas
    input_string = input_string.lower()
    
    # Recorre cada carácter de la cadena
    for char in input_string:
        if char.isalpha():  # Verifica si el carácter es una letra
            char_count[char] = char_count.get(char, 0) + 1
    
    # Busca el carácter mayoritario
    majority_char = None
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            majority_char = char
            max_count = count
    
    # Si se encontró un carácter mayoritario, muéstralo, de lo contrario, indica que no hay carácter mayoritario
    if majority_char is not None:
        messagebox.showinfo("Resultado", f'El carácter mayoritario es "{majority_char}"')
    else:
        messagebox.showinfo("Resultado", "No hay carácter mayoritario")

def main():
    # Crea una ventana principal
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    try:
        # Solicita al usuario ingresar una palabra
        input_word = simpledialog.askstring("Palabra", 'Ingrese una palabra:')
        
        # Verifica si la entrada contiene al menos una letra
        if any(char.isalpha() for char in input_word):
            findMajorityChar(input_word)
        else:
            messagebox.showerror("Error", "Ingrese una palabra que contenga al menos una letra.")

    except TypeError:
        messagebox.showerror("Error", "Ingrese una palabra válida.")

    root.mainloop()

if __name__ == '__main__':
    main()
