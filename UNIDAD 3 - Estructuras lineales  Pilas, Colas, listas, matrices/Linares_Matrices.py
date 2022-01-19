#Matrices

#4
"""4 - Escribir una función sumaLista() y una función
multiplicaLista() que sumen y multipliquen
respectivamente todos los números de una lista.
Ej: sumaLista([1,2,3,4])=10 y multiplicaLista([1,2,3,4]) = 24 """

def sumaLista(c:list)->int:
    suma = 0
    for i in range(len(c)):
        suma = c[i] + suma
    return suma
        
    
    
assert sumaLista([1,2,3,4]) == 10

print(sumaLista([1,2,3,4]))

print(sumaLista([1,2,3,4,1]))


def multiplicaLista(c:list)->int:
    multiplica = 1
    for i in range(len(c)):
        multiplica = c[i] * multiplica
    return multiplica
        
    
    
assert multiplicaLista([1,2,3,4]) == 24

print(multiplicaLista([1,2,3,4]))

print(multiplicaLista([1,2,3,4,2]))

#7
"""7 - Escribir un programa que almacene los vectores
(1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
El producto escalar entre dos vectores a=(a1,a2,..,an) y b=(b1,b2,..,bn) se define así a*b=a1*b1+a2*b2+..+an*bn. 
Ej: a=(1,2) y b=(3,4) ->  a*b = 1*3 + 2*4 = 11"""

def producto_escalar(a:list,b:list)->int:
    lista1 = [1,2,3]
    lista2 = [-1,0,2]
    
    print(lista1[0]*lista2[0]+lista1[1]*lista2[1]+lista1[2]*lista2[2])
    
a = [1,2,3]
b = [-1,0,2]    
producto_escalar(a,b)

#11
"""11 - Programar una función enumF que tome una
matriz y numere cada celda de la matriz en orden
creciente de izquierda a derecha y de arriba a abajo
y otra enumC que numere cada celda de la matriz en
orden creciente de arriba a abajo luego izquierda a derecha.

Ej: enumF(a)  1 2 3   enumC(a)= 1 3 5
              4 5 6             2 4 6
"""
 
 
def filas(A): #devuelve la cantidad de filas (o m) de la matriz
    return len(A)

def columnas(A): #devuelve la cantidad de columnas (o n) de una matriz
    return len(A[0])

def dimension(A):
    return (filas(A),columnas(A))


def enumF(A):
    c=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            c=c+1
            print(c,end="")
        print()

                
enumF([[1,1,1],[1,1,1],[1,1,1]])

def enumC(A):
    
    columna = 1
    fila = 0
    for i in range(len(A)):
        fila = fila + 1
        for j in range(len(A[0])):
            columna=columna+len(A)
            print(columna-((len(A[0]))),end="")
        columna = fila + 1
        print()
        
print(enumC([[1,1,1],[1,1,1],[1,1,1]]))
    

    
#14

"""
Escriba una función que tome una matriz cuadrada (n y m son iguales) y
devuelva una lista con la diagonal de esa matriz (la diagonal es cuando recorro la matriz e i==j) 
otra que sume los elementos de esa lista. diagonal() y sumaDiagonal()
https://es.wikipedia.org/wiki/Diagonal_principal"""

c = [[1,3,5],
     [4,3,5],
     [2,1,2]] # 3 filas x 3 columnas

def diag(M): #
    (n_filas,n_columnas) = dimension(M)# asigno a la tupla (n_filas,n_columnas) la dimension de la matriz M
    lista = []#creo una lista vacia
    if n_filas == n_columnas:#si el numero de filas coincide con el numero de columnas
        for i in range (n_filas):#itero con i en el rango de filas
            lista.append(M[i][i])#agrego a la lista vacia los elementos ubicados en la posicion i==j
    return lista

def sum_diag(M)->int:
    sum = 0
    for i in diag(M):
        sum = sum + i
    return sum

assert diag (c) == [1,3,2]
assert sum_diag (c) == 6


a = [[1,2],[3,4]]
print(diag(a)) 
print(sum_diag(a))



    
    
    
    
    
    

