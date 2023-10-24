class Graph:
    # Constructor
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]  # Crea una lista de adyacencia vacía con n vértices (municipios).
        
        # Agrega bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)  # Agrega el destino a la lista de adyacencia 
            self.adjList[dest].append(src)  # Agrega el origen a la lista de adyacencia

# Función para verificar si asignar una persona a un vértice es segura
def isSafe(graph, persona, v, c):
    for u in graph.adjList[v]:  # Itera a través de los vértices adyacentes a v en el grafo.
        if persona[u] == c:  # Si un vértice adyacente ya tiene el mismo persona, no es seguro.
            return False
    return True

# Función principal para encontrar una asignación de personas para el grafo
def kPerson(g, persona, k, v, n):
    if v == n:  # Si hemos asignado personas a todos los vértices, imprimimos la asignación de personas y retornamos.
        print([persona[v] for v in range(n)])  # Muestra los personas asignados a cada vértice.
        return

    for c in range(1, k + 1):  # Intenta asignar persona del 1 al k.
        if isSafe(g, persona, v, c):  # Si es seguro asignar el persona c al vértice v.
            persona[v] = c  # Asigna el persona c al vértice v.
            kPerson(g, persona, k, v + 1, n)  # Llama a la función recursivamente para el siguiente vértice.
            persona[v] = 0  # Restablece el persona del vértice v a 0 (sin persona) para explorar otras opciones.

if __name__ == '__main__':
    n = int(input("Ingrese el número de municipios (n): "))  # Lee el número de vértices del usuario.
    k = int(input("Ingrese el número de personas (k): "))  # Lee el número de persona del usuario.
    persona = ['', ]  # Inicializa una lista para almacenar los nombres de personas.

    for i in range(k):
        nombre_persona = input(f"Ingrese el nombre de la persona {i + 1}: ")  # Lee el nombre de cada persona.
        persona.append(nombre_persona)  # Agrega el nombre de la persona a la lista de personas.
    print(persona)
        
    edges = []  # Inicializa una lista para almacenar los bordes del grafo.
    num_edges = int(input("Ingrese la cantidad de aristas en la lista de adyacencia: "))  # Lee el número de bordes del usuario.

    for i in range(num_edges):
        src, dest = map(int, input(f"Ingrese el número {i + 1} (separados por espacio): ").split())
        edges.append((src, dest))  # Agrega la arista (src, dest) a la lista de bordes.

    g = Graph(edges, n)  # Crea un objeto Graph con la lista de bordes y el número de vértices.
    persona = [0] * n  # Inicializa una lista de personas con valores 0 para los vértices.
    kPerson(g, persona, k, 0, n)  # Llama a la función kPerson para encontrar una asignación de personas.
