# dada las funciónes
from typing import List,Tuple
Matrix = List[List[int]]

def filas(A:Matrix)->int: #devuelve la cantidad de filas (o m) de la matriz
    return len(A)

def columnas(A:Matrix)->int: #devuelve la cantidad de columnas (o n) de una matriz
    return len(A[0])

def dimension(A:Matrix)->Tuple[int,int]: # Devuelve una tupla (un par) con el valor (filas,columnas)
    return (filas(A),columnas(A))

"""
Las matrices simétricas son matrices donde para todo elemento de la matriz a[i][j] == a [j][i],
fíjense que esto funciona si la matriz es cuadrada, filas(M) = columna(M)
Escriba una función que tome una matriz cuadrada (n y m son iguales) y
devuelva si es simétrica o no.
"""
M1 = [[1,3,5],
      [4,3,5],
      [2,1,2]] # 3 filas x 3 columnas

M2 = [[1,2,3],
      [2,3,5],
      [3,5,2]] # 3 filas x 3 columnas


M3 = [[0,5,9],
      [5,3,5],
      [9,5,2]]

def matriz_simetrica(M:Matrix)->bool:
    
    
    
        resultado = True
        for i in range(filas(M)):
            
            for j in range(columnas(M)):
                if M[i][j]!=M[j][i]:
                    
                    resultado = False
                    break
        return resultado
    
    
    
assert matriz_simetrica(M1) == False
assert matriz_simetrica(M2) == True
assert matriz_simetrica(M3) == True

print(matriz_simetrica(M1))
print(matriz_simetrica(M2))



