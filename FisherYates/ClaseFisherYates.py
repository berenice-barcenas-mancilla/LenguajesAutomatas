from random import randrange

#funcionde utukudad para intercambiar elementos a[i] y a[j] en una lista

def swap(A,i,j):
    temp =A[i]
    A[i]=A[j]
    A[j]=temp
    
#funcion para trabajar con una lista A
def shuffle(A):
    #lista de lectura desde el indice mas abajo hasta el mas alto
    for i in range(len(A)):
        #genera un numero aleatorio j tal que i<=j<n
        j=randrange(i,len(A))
        #realiza un intercambio el elemento actual con el indice generado aleatoriamente 
        swap(A,i,j) 
        
if __name__=='__main__':
    A=[1,2,3,4,5,6]
    shuffle(A)
    
    #imprime la lista barajada
    print(A)