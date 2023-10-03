import sys

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    for (u, w) in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    time = time + 1
    return time

def findLongestDistance(graph, source, n):
    departure = [-1] * n
    discovered = [False] * n
    time = 0

    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)

    cost = [sys.maxsize] * n
    cost[source] = 0

    for i in reversed(range(n)):
        v = departure[i]
        for (u, w) in graph.adjList[v]:
            w = -w
            if cost[v] != sys.maxsize and cost[v] + w < cost[u]:
                cost[u] = cost[v] + w

    for i in range(n):
        print(f'dist({source},{i})={-cost[i]}')

if __name__ == '__main__':
    # Pregunta al usuario cuántos tripletes va a ingresar
    num_triplets = int(input("Ingrese el número de tripletes: "))
    
    # Crea un arreglo vacío para almacenar los tripletes ingresados por el usuario
    triplets = []
    
    # Ingresa los tripletes separados por comas con ventanas
    for _ in range(num_triplets):
        triplet_str = input("Ingrese el triplete (source, dest, weight) separado por comas: ")
        triplet = tuple(map(int, triplet_str.split(',')))
        triplets.append(triplet)

    # Calcula el tamaño del grafo basándose en los vértices presentes en los tripletes
    vertices = set()
    for triplet in triplets:
        vertices.add(triplet[0])
        vertices.add(triplet[1])
    
    n = max(vertices) + 1
    
    graph = Graph(triplets, n)
    source = 7
    findLongestDistance(graph, source, n)
