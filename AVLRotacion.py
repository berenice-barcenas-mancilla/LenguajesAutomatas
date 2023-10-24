class NodoAVL:  #Definición de la clase NodoAVL que representa un nodo en un árbol AVL
    def __init__(self, clave):
        self.clave = clave       #Valor almacenado en el nodo
        self.altura = 1          #Altura del nodo, inicializada en 1
        self.izquierda = None    #Referencia al hijo izquierdo
        self.derecha = None      #Referencia al hijo derecho

def altura(nodo): #Función que actualiza la altura de un nodo basándose en las alturas de sus hijos
    if nodo is None:
        return 0
    return nodo.altura

def actualizar_altura(nodo): #Función que realiza una rotación simple a la izquierda en un árbol AVL
    if nodo is not None:
        nodo.altura = 1 + max(altura(nodo.izquierda), altura(nodo.derecha))

def rotacion_izquierda(nodo_y): #Función que realiza una rotación simple a la izquierda en un árbol AVL
    if nodo_y is None or nodo_y.derecha is None:
        return nodo_y

    nodo_x = nodo_y.derecha
    nodo_t = nodo_x.izquierda
    nodo_x.izquierda = nodo_y
    nodo_y.derecha = nodo_t

    actualizar_altura(nodo_y)
    actualizar_altura(nodo_x)

    return nodo_x

def rotacion_derecha(nodo_x): #Función que realiza una rotación simple a la derecha en un árbol AVL
    if nodo_x is None or nodo_x.izquierda is None:
        return nodo_x

    nodo_y = nodo_x.izquierda
    nodo_t = nodo_y.derecha
    nodo_y.derecha = nodo_x
    nodo_x.izquierda = nodo_t

    actualizar_altura(nodo_x)
    actualizar_altura(nodo_y)

    return nodo_y

def rotacion_doble_izquierda(nodo_z): #Función que realiza una rotación doble a la izquierda en un árbol AVL
    if nodo_z is None or nodo_z.derecha is None:
        return nodo_z

    nodo_z.derecha = rotacion_derecha(nodo_z.derecha) 
    return rotacion_izquierda(nodo_z)

def rotacion_doble_derecha(nodo_z): #Función que realiza una rotación doble a la derecha en un árbol AVL
    if nodo_z is None or nodo_z.izquierda is None:
        return nodo_z

    nodo_z.izquierda = rotacion_izquierda(nodo_z.izquierda)
    return rotacion_derecha(nodo_z)
 
def es_arbol_avl(nodo): #Función que verifica el balance del arbol
    if nodo is None:
        return True

    balance_factor = altura(nodo.izquierda) - altura(nodo.derecha) #Verifica el balance del árbol calculando el factor de equilibrio
    if abs(balance_factor) > 1:
        return False

    return es_arbol_avl(nodo.izquierda) and es_arbol_avl(nodo.derecha) #Verifica si el subárbol izquierdo y el subárbol derecho también son AVL


def imprimir_arbol(nodo, nivel=0, prefijo="Raíz: "): #Función que imprime el árbol en formato jerárquico
    if nodo is not None:
        print(" " * (nivel * 4) + prefijo + str(nodo.clave) + " (" + str(nodo.altura) + ")")
        imprimir_arbol(nodo.izquierda, nivel + 1, "Izq: ")
        imprimir_arbol(nodo.derecha, nivel + 1, "Der: ")

#Ejemplo preestablecido de un árbol AVL
raiz = NodoAVL(10)  #Nodo raíz
#raiz.izquierda = NodoAVL(20) #Nodo hijo izquierdo de la raíz
raiz.derecha = NodoAVL(20)  #Nodo hijo derecho de la raíz
#raiz.izquierda.izquierda = NodoAVL(10) #Nodo hijo izquierdo del nodo hijo izquierdo 
#raiz.izquierda.derecha = NodoAVL(15)   #Nodo hijo derecho del nodo hijo izquierdo 
raiz.derecha.derecha = NodoAVL(30)    #Nodo hijo derecho del nodo hijo derecho 
#raiz.derecha.izquierda = NodoAVL(20)    #Nodo hijo derecho del nodo hijo derecho 

continuar = True

while continuar:
    tipo_rotacion = input("\nSeleccione el tipo de rotación (LL, RR, RL, LR) o 'no' para salir: ")

    if tipo_rotacion.lower() == "no":
        continuar = False
        print("\nGracias por su atención a la presentación de Rotación de Árboles AVL")
    else:
        print("\nÁrbol AVL antes de rotaciones:")  #Imprime el árbol antes de las rotaciones
        imprimir_arbol(raiz)

        if tipo_rotacion == "RR":  #rotacion simple derecha
            raiz = rotacion_izquierda(raiz)
        elif tipo_rotacion == "LL":  #rotacion simple izquierda
            raiz = rotacion_derecha(raiz)
        elif tipo_rotacion == "LR":  #rotacion doble izquierda derecha
            raiz = rotacion_doble_izquierda(raiz)
        elif tipo_rotacion == "RL":  #rotacion doble derecha izquierda
            raiz = rotacion_doble_derecha(raiz)

        if es_arbol_avl(raiz):  #Verifica si el árbol sigue siendo AVL después de la rotación

            print("\nÁrbol AVL después de la rotación:")
            imprimir_arbol(raiz)
        else:
            print("\nError: El árbol ya no es AVL después de la rotación.")
