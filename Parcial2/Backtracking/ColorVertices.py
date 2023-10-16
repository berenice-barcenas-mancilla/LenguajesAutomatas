class Graph:
    # Constructor
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]  # Crea una lista de adyacencia vacía con n vértices.
        # Agrega bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)  # Agrega el destino a la lista de adyacencia 
            self.adjList[dest].append(src)  # Agrega el origen a la lista de adyacencia

# Función para verificar si asignar un color a un vértice es seguro
def isSafe(graph, color, v, c):
    for u in graph.adjList[v]:  # Itera a través de los vértices adyacentes a v en el grafo.
        if color[u] == c:  # Si un vértice adyacente ya tiene el mismo color, no es seguro.
            return False
    return True

# Función principal para encontrar una asignación de colores para el grafo
def kColorable(g, color, k, v, n):
    if v == n:  # Si hemos coloreado todos los vértices, imprimimos la asignación de colores y retornamos.
        print([COLORS[color[v] - 1] for v in range(n)])  # Muestra los colores asignados a cada vértice.
        return

    for c in range(1, k + 1):  # Intenta asignar colores del 1 al k.
        if isSafe(g, color, v, c):  # Si es seguro asignar el color c al vértice v.
            color[v] = c  # Asigna el color c al vértice v.
            kColorable(g, color, k, v + 1, n)  # Llama a la función recursivamente para el siguiente vértice.
            color[v] = 0  # Restablece el color del vértice v a 0 (sin color) para explorar otras opciones.

if __name__ == '__main__':
    n = int(input("Ingrese el número de vertices(n): "))  # Lee el número de vértices del usuario.
    k = int(input("Ingrese el número de colores (k): "))  # Lee el número de colores del usuario.
    COLORS = []  # Inicializa una lista para almacenar los nombres de colores.

    for i in range(k):
        color = input(f"Ingrese el nombre del color {i + 1}: ")  # Lee el nombre de cada color.
        COLORS.append(color)  # Agrega el nombre del color a la lista COLORS.

    edges = []  # Inicializa una lista para almacenar los bordes del grafo.
    num_edges = int(input("Ingrese la lista adyacente: "))  # Lee el número de bordes del usuario.

    for i in range(num_edges):
        src, dest = map(int, input(f"Ingrese {i + 1} (separados por espacio): ").split())
        edges.append((src, dest))  # Agrega la arista (x,y) a la lista de bordes.

    g = Graph(edges, n)  # Crea un objeto Graph con la lista de bordes y el número de vértices.
    color = [None] * n  # Inicializa una lista de colores con valores nulos para los vértices.
    kColorable(g, color, k, 0, n)  # Llama a la función kColorable para encontrar una asignación de colores.
