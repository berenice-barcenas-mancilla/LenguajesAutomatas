import sys
from collections import deque

# Un nodo de queue utilizado en BFS
class Node:
    
    # (x, y) representa las coordenadas del tablero de ajedrez
    # 'dist' representa su distancia mínima desde la fuente
    
    def __init__(self, x, y, dist=0):  # Cambio de '_init_' a '__init__'
        self.x = x
        self.y = y
        self.dist = dist
    
    # Como estamos usando 'Node' como una clave en un diccionario,
    # necesitamos anular las funciones '__hash__' y '__eq__' en lugar de '_hash_' y '_eq_'
    
    def __hash__(self):
        return hash((self.x, self.y, self.dist))
    
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
    
# Las siguientes listas detallan los ocho movimientos posibles para un caballo
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

# Comprueba si (x, y) son coordenadas de tablero de ajedrez válidas.
# Tenga en cuenta que un caballo no puede ir fuera del tablero de ajedrez
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)

# Encuentra el camino mínimo entre una fuente dada
# y una celda de destino dada
def findShortestDistance(src, dest, N):
    # Configurando para verificar si la celda de la matriz se ha visitado antes o no
    visited = set()
    
    # Crear una cola y encolar la celda de origen con distancia 0
    q = deque()
    q.append(src)
    
    # Bucle hasta que la cola esté vacía
    while q:
        # Sacar el primer elemento de la cola
        node = q.popleft()
        x = node.x
        y = node.y
        dist = node.dist
        
        # Si la celda de destino es alcanzada, devuelva su distancia
        if x == dest.x and y == dest.y:
            return dist
        
        # De lo contrario, para cada movimiento posible para un caballo,
        # obtener la coordenada del tablero de ajedrez correspondiente y
        # si no se ha visitado antes, encolarla y marcarla como visitada
        if node not in visited:
            visited.add(node)
        
        for i in range(len(row)):
            # Obtener la coordenada del tablero de ajedrez correspondiente
            x1 = x + row[i]
            y1 = y + col[i]
            
            if isValid(x1, y1, N):
                q.append(Node(x1, y1, dist + 1))
            
    return sys.maxsize

if __name__ == '__main__':  # Cambio de '_name_' a '__name__'
    N = 8
    src = Node(0, 7)
    dest = Node(7, 0)
    print("El número de pasos mínimos requeridos es", findShortestDistance(src, dest, N))
