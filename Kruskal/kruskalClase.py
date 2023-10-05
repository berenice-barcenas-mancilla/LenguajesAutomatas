#una clase para representar un conjunnto disjunto
class DisjointSet:
    parent = {}
    
    #realiza la operacion de Makeset
    def makeSet(self,n):
        #crea n conjuntos disjuntos (uno para cada vertice)
        for i in range(n):
            self.parent[i]=i
        
    #encuentra la raizdel conjunto al que pertenece el elemento k
    def find(self, k):
        #si k es root
        if self.parent[k]==k:
            return k
                
         # recurre para el padre hasta que encontramos la raíz
        return self.find(self.parent[k])

    #tralizar la union de dos subconjuntos
    def union(self, a, b):
            #encontrar la ri sw loa conjuntos a los que perteneecen los elementos x e y
            x=self.find(a)
            y=self.find(b)
            
            self.parent[x]=y
            
def runKruskalAlgorithm(edges,n):
    #almacena los bordes presentes en MTS
    MST =[]
        
    #Inicializaar la clase distJoinSet
    #Crea un conjunto para cada elemento del universo
        
    ds=DisjointSet()
    ds.makeSet(n)
        
    index = 0
        
    #ordena los bordes aumentando el peso
    edges.sort(key=lambda x:x[2])
        
    #MST contiene exactamente las aristas V-1
    while len(MST)!=n-1:
        
        #considerar el borde siguiente con peso minimo del graph 
        (src, dest, weight)=edges[index]
        index =index+1
        
        #encontrar la raiz de los conjuntos a los que se unen dos extremos
        #vertices de la siguiente arisra pertenecen
        x=ds.find(src)
        y=ds.find(dest)
        
        #si ambos extremos tienen diferentes padres pertenecen a 
        #diferentes componentes conectados y se pueden incluir en MST
        if x!=y:
            MST.append((src,dest,weight))
            ds.union(x,y)
    return MST
    
if __name__ == '__main__':
    
    #(u,v,w) el triplete representa un borde no dirgido desde
    #vertice u a vertice v con peso 
    edges = [
        (0,1,7),(1,2,8),(0,3,5),
        (1,3,9),(1,4,7),(2,4,7),
        (2,4,5),(3,4,15),(3,5,6),
        (4,5,8),(4,6,9),(5,6,11)
    ]
        
        
    n=7
    e = runKruskalAlgorithm(edges, n)
    print(e)

