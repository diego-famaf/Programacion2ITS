

#6 Defina en python todas las funciones anteriores

#Factorial de un numero entero
def factorial(a:int)->int:
    
    if a == 0:
        solucion = 1
    else:
        solucion = a * factorial(a-1)
    
    return solucion

print("factorial de un n° entero")
print(factorial(5))

#Producto de una lista de números:
def product(a:list)->int:
    
    if a == []:
        solucion =  1
    else:
        solucion = a[0] * product(a[1:])
        
    return solucion 

print("producto de una lista de numeros")

print(product([5,2,6,8,3]))   

#Longitud de una lista:


def longitud_lista(a:list)->int:
    if a == []:
        solucion = 0
    else:
        solucion = 1 + longitud_lista(a[1:])
    return solucion

print("longitud de una lista,[5,2,6,8,3]:")

print(longitud_lista([5,2,6,8,3]))

#Inversa de una lista:



def inversa(a:list)->list:
    if a==[]:
        solucion = []
    else:
        solucion = inversa(a[1:]) + [a[0]]
    return solucion

print("inversa de una lista:")

print(inversa([5,2,3]))

#Eliminación de elementos iniciales:
"""drop :: Int -> [a] -> [a]
drop 0 xs     = xs
drop n []     = []
drop n (x:xs) = drop (n-1) xs"""

def drop(a:int,b:list)->list:
    if a == 0:
        solucion = b
    elif b==[]:
        solucion = []
    else:
        solucion = drop((a-1),(b[1:]))
        
    return solucion

print("Eliminacion de elementos iniciales:")

print(drop(3,[4,5,2,6,8,3]))


#4 Recursión múltiple
#Fibonacci


def fibonacci(a:int)->int:
    if a == 0:
        solucion = 0
    elif a == 1:
        solucion = 1
    else:
        solucion = fibonacci(a-2) + fibonacci (a-1)
    return solucion

print("fibonacci:")

print(fibonacci(8))


#Subir la escalera


def formas(a:int)->int:
    if a == 1:
        solucion = 1
    elif a == 2:
        solucion = 2
    else:
        solucion = formas(a-1) + formas (a-2)
    return solucion

print("subir la escalera:")

print(formas(5))


#5 Recursión mutua
#Par e impar por recursión mutua:


def par(a:int)->bool:
    if a==0:
        solucion=True
    else:
        solucion = impar(a-1)
    return solucion

def impar(a:int)->bool:
    if a==0:
        solucion=False
    else:
        solucion = par(a-1)
    return solucion

print("Par e Impar por recursion mutua:")

print(par(7))
print(impar(8))
print(par(8))
print(impar(7))

