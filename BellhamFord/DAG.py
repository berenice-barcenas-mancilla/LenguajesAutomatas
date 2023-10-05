import sys
#una clase para representar un objeto graph
class Graph:
    #constructor
    def __init__(self, edges, n):
        #una lista de para representar una lista de adyacencia
        self.adjList=[[] for _ in range(n)]
        #agrega bordes al graph dirijido
        for(source,dest,weight)in edges:    
            self.adjList[source].append((dest,weight))
#realice dfs en el graph y establezca la hora de salida de todos
#vertices del graph
def DFS(graph, v, discovered, departure, time):
    # marca el nodo actual como descubierto
    discovered[v] = True

    # realiza DFS para cada arista (v, u)
    for (u, w) in graph.adjList[v]:
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)

    # actualiza el tiempo de salida después de explorar todas las aristas
    departure[time] = v
    time = time + 1
    return time

def findLongestDistance(graph,source,n):
        #departuew almacena el numero de vertice que tiene su salida
        #tiempo igual al inidice de la misma
        departure=[-1]*n
        #para realizar un seguimiento de si se descubre un vertice o no
        discovered = [False]*n
        time=0

        for i in range(n):
            if not discovered[i]:
                time=DFS(graph,i,discovered,departure,time)
                
        cost = [sys.maxsize]*n
        cost[source]=0
        
        for i in reversed(range(n)):
            v=departure[i]
            for(u,w)in graph.adjList[v]:
                w = -w
                if cost[v]!=sys.maxsize and cost[v]+w<cost[u]:
                    cost[u]=cost[v]+w
        
        for i in range(n):
            print(f'dist({source},{i})={-cost[i]}')

if __name__ == '__main__':
    edges = [
        (0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5),
        (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)
    ]

    n = 8
    graph = Graph(edges, n)
    source = 7
    findLongestDistance(graph, source, n)
