# 1 Ejercicio aritmética:

Escriba un programa que pida dos números y que escriba su media aritmética.

Se recuerda que la media aritmética de dos números es la suma de ambos números dividida por 2

"""def promedio(a:int,b:int)->float:
    return (a+b)/2

guardar = input("Ingrese el primer numero: ")
primer_numero = int(guardar)
segundo_numero = int(input("Ingrese el segundo número: "))
print("El promedio es: ",promedio(primer_numero,segundo_numero))
"""

# 2 Expresion Booleana: escriba en python: "A es mayor a B y B es mayor a C"
# A > B and B > C

# 3 Defina una funcion "es_par" que tome un numero entero y devuelva True si el número es par y devuelva False si el número es impar.
def es_par (a:int)->bool:
    return a % 2 == 0

assert es_par(2) == True
assert es_par(2) == True

# 4 Ejercicio if

"""Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

COMPARADOR DE NÚMEROS
Escriba un número: 23
Escriba otro número: 14.5
Menor: 14.5; Mayor: 23.0"""

"""#
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print ("Menor: ",b, "Mayor: ",a)
elif a < b:
    print ("Menor: ",a, "Mayor: ",b)
else:
    print ("Los números son iguales")
"""

# 5 if (2)
Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.

DIVISOR DE NÚMEROS
Escriba el dividendo: 14
Escriba el divisor: 5
La división no es exacta. Cociente: 2 Resto: 4

# 6 Ejercicio for: Escriba una función que tome 2 numeros y cuente cuantos numeros pares hay entre los dos.

"""
def cuantos_pares(a:int,b:int)->int:
    n = 0
    for i in range (a,b):
        if es_par(i): # o i%2!=0
            n = n+1
    return n

print(cuantos_pares(4,8))
"""

# 7 Ejercicio while
"""Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí 

DIGA sí PARA CONTINUAR
¿Desea continuar el programa?: sí
¿Desea continuar el programa?: sí
¿Desea continuar el programa?: NO
¡Hasta la vista!"""

"""
while True:
    respuesta = input("Desea continuar?:").lower()
    if respuesta != "si":
        break
    
print ("Hasta la vista")
"""

# 8 ejercicio funcion
"""
Defina una función que diga si un año es bisiesto:
Escriba un programa que pida un año y que escriba si es bisiesto o no.

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
"""

"""
def bisiesto(a:int)-> bool:
    return ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0)

print(bisiesto(2012))
print(bisiesto(2010))
print(bisiesto(2000))
print(bisiesto(1900))
"""

# 9 Ejercicios strings:  Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman.
"""
def riman(palabra1,palabra2)->str:
    rebanada1 = palabra1[-3:]
    rebanada2 = palabra2[-3:]
    return rebanada1 == rebanada2

print (riman ("casa","tasa") )
"""

# 10 Escriba un programa que pida una frase y una vocal y cambie todas las vocales de la frase por la vocal (una forma de hacerlo es convertir la frase en una lista y hacer el cambio en la lista.

"""
def reemplazar_vocal(frase:str,vocal:str)->str:
    respuesta = []
    for letra in frase:
        if letra in ['a','e','i','o','u']:
            respuesta.append(vocal)
        else:
            respuesta.append(letra)
    return "".join(respuesta)
            
print(reemplazar_vocal ("Cumpleaños feliz",'a')) # "Camplaañas falaz"
"""

# 11 Ejercicio lista: hacer una funcion que tome una lista y me devuelva otra lista solo con los elementos pares
"""
def pares (lista:list)->list:
    r = []
    for numero in lista:
        if numero %2 == 0:
            r.append(numero)
    return r
    
assert pares([1,2,3,4,5,6,7,8,9]) == [2,4,6,8]
"""

# 12 Ejercicio diccionario: hacer una función que tome el diccionario de poblacion de latam, devolver el nombre del país con mayor población.
def mayor_poblacion(poblacion:dict)->str:
    poblacion_max = 0
    pais = ""
    for clave in poblacion:
        if poblacion[clave] > poblacion_max:
            poblacion_max = poblacion[clave]
            pais = clave
    return pais
    

poblacion = {"Brasil": 210147125,
             "Colombia": 50372424,
             "Argentina" :44938712}

print (mayor_poblacion(poblacion))