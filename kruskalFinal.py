# Importar la biblioteca tkinter para la GUI
import tkinter as tk
from tkinter import simpledialog, messagebox

# Definir una clase para conjuntos disjuntos (Disjoint Set)
class DisjointSet:
    parent = {}  # Diccionario para almacenar los padres de cada elemento
    
    # Método para inicializar un conjunto
    def makeSet(self, n):
        for i in range(n):
            self.parent[i] = i  # Cada elemento es su propio padre al principio
    
    # Método para encontrar el representante (raíz) de un conjunto
    def find(self, k):
        if self.parent[k] == k:
            return k  # Si el elemento es su propio padre, es la raíz
        return self.find(self.parent[k])  # De lo contrario, buscar el padre del padre
    
    # Método para unir dos conjuntos
    def union(self, a, b):
        x = self.find(a)  # Encontrar el representante de a
        y = self.find(b)  # Encontrar el representante de b
        self.parent[x] = y  # Establecer el representante de a como el padre de b

# Función para ejecutar el algoritmo de Kruskal
def runKruskalAlgorithm(edges):
    MST = []  # Lista para almacenar el árbol de expansión mínima (Minimum Spanning Tree)
    ds = DisjointSet()  # Instancia de la clase DisjointSet
    ds.makeSet(len(edges))  # Inicializar conjuntos para cada vértice
    edges.sort(key=lambda x: x[2])  # Ordenar las aristas por peso
    
    for edge in edges:
        (src, dest, weight) = edge  # Desempacar la arista en sus componentes
        x = ds.find(src)  # Encontrar el representante del vértice fuente
        y = ds.find(dest)  # Encontrar el representante del vértice destino
        
        if x != y:
            MST.append((src, dest, weight))  # Agregar la arista al MST
            ds.union(x, y)  # Unir los conjuntos de src y dest en el conjunto DisjointSet
    return MST


# Punto de entrada del programa
if __name__ == '__main__':
    edges = []  # Lista para almacenar las aristas
    n = int(simpledialog.askstring("Input", "Ingrese la cantidad de tripletes:"))  # Solicitar al usuario el número de tripletes
    triplets_input = []  # Lista para almacenar los tripletes ingresados

    for i in range(n):
        triplet = simpledialog.askstring("Input", f"Ingrese el triplete {i+1} (x,y,w) separado por comas:")  # Solicitar al usuario ingresar un triplete
        triplet = triplet.split(',')  # Dividir el triplete en sus componentes
        if len(triplet) != 3:
            messagebox.showerror("Error", "Cada triplete debe tener tres valores (x,y,w).", icon='error')  # Mostrar un error si el triplete no tiene tres valores
            exit()  # Salir del programa si hay un error
        edges.append((int(triplet[0]), int(triplet[1]), int(triplet[2])))  # Agregar la arista a la lista de aristas
        triplets_input.append(triplet)  # Agregar el triplete ingresado a la lista

    # Mostrar los tripletes ingresados en una ventana
    triplets_str = "\n".join([f"({triplet[0]},{triplet[1]},{triplet[2]})" for triplet in triplets_input])
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Tripletes ingresados", f"Tripletes ingresados:\n{triplets_str}", icon='info')  # Mostrar los tripletes ingresados

    result = runKruskalAlgorithm(edges)  # Ejecutar el algoritmo de Kruskal

    result_str = ""
    for edge in result:
        result_str += f"({edge[0]},{edge[1]},{edge[2]}), "  # Crear una cadena de texto con las aristas del MST

    result_str = result_str[:-2]  # Eliminar la última coma y espacio

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Resultado", f"Resultado:\n({result_str})", icon='info')  # Mostrar el MST resultante
