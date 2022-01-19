#Ejercicio 1
print("Hola Mundo")

#Ejercicio 2
def sumarab(a:int,b:int)-> int:
    return(a + b)
assert(sumarab(3,5))==8
assert(sumarab(0,0))!=8 
print(sumarab(3,3))

#Ejercicio 3
def mayor(a: int,b: int)-> int:
    if a>b:
        return (a)
    else:
        return (b)
assert mayor(3,8) == 8
assert mayor(5,6) != 5
print(mayor(5,4))

#Ejercicio 4
def max_de_tres(a:int,b:int,c:int)-> int:
    if a>b and a>c:
        return(a)
    elif b>a and b>c:
        return(b)
    else:
        return(c)
assert max_de_tres(2,6,-1) == 6
assert max_de_tres(2,0,-1) == 2
print(max_de_tres(3,-1,2))

#Ejercicio 5
def entre0y10(a: int)->bool:
    if(a<=10 and a>=0):
        return (True)
    else:
        return (False)
assert entre0y10(5) == True
assert entre0y10(11) == False     
print(entre0y10(0))

#Ejercicio 6
def entreAyB(a: int, b: int, c:int)->bool:
    if(c>a and c<b):
        return(True)
    else:
        return(False)
assert entreAyB (1,6,3) == True
assert entreAyB (1,6,9) == False
print(entreAyB(11,20,15))

#Ejercicio 7
def mensaje(c):
    if entreAyB(11,20,c):
        print("un mensaje")
    elif entreAyB(21,30,c):
        print("otro mensaje")
    else:
        print("otro mas")
        
mensaje(14)
mensaje(123)
mensaje(23)

#Ejercicio 8
i=1
while (i<=100):
    print(i)
    i+=1
    
#Ejercicio 9
for i in range(0,100):
    print (i+1)
#Ejercicio 10
def par(a:int)->bool:
    if (a%2==0):
        return(True)
    else:
        return(False)
    
assert par (3) == False
assert par (2) == True
print(par(7))

#Ejercicio 11
for i in range(1,101):
    if par(i):
        print(i)

#Ejercicio 12
import random
numero = random.randint(5, 10)

print(numero)
    

    
