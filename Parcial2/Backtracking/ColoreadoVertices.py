class Graph:
    #constructor
    def __init__(self,edges,n):
        self.adjList=[[]for _ in range(n)]
        #agrega bordes al graph no dirigido
        for (src,dest)in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)    
            
# Función para verificar si asignar un color a un vértice es seguro
def isSafe(graph, color, v, c):
    for u in graph.adjList[v]:
        if color[u]==c:
            return False
    return True

# Función principal para encontrar una asignación de colores para el grafo
def kColorable(g,color,k,v,n):
    if v==n:
        print([COLORS[color[v]]for v in range(n)])
        return 
    
    for c in range(1,k+1):
        if isSafe(g,color,v,c):
            color[v]=c
            kColorable(g, color, k, v + 1, n)
            color[v]=0

if __name__ == '__main__':
    edges = [
        (0, 1), (0, 4), (0, 5), (4, 5),
        (1, 4), (1, 3), (2, 3), (2, 4)
    ]

    COLORS = ['BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK', 'BLACK', 'BROWN', 'WHITE', 'PURPLE']
    n = 6 #vetices
    g = Graph(edges, n) 
    k = 3
    color = [None] * n
    kColorable(g, color, k, 0, n)

    