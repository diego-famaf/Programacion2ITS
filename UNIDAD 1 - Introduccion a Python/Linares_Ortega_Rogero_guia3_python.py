#Ejercicio 1
def reverse_range()->list:
    Lista = [0,1,2,3,4,5,6,7,8,9,10]
    nuevaLista = list(reversed(Lista))
    return(nuevaLista)
assert reverse_range() == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(reverse_range())
#Ejercicio 2
def suma(a:[int])->int:
    count = 0
    for i in range(len(a)):
        count = count + a[i] 
    return (count)
assert suma([1,2,3,4]) == 10
assert suma([1,2,3,5]) != 10

print(suma([1,3,4,15]))

#Ejercicio 3
def mul(a:[int])->int:
    count = 1
    for i in range(len(a)):
        count = count * a[i] 
    return (count)
assert mul([1,2,3,4]) == 24
assert mul([1,2,3,5]) != 24

print(mul([1,2,3,4]))
#Ejercicio 4
def longitud(a:list)->int:
    count=0
    for i in a:
        count = count + 1
    return(count)
assert longitud([1,2,3,4]) == 4
assert longitud([]) == 0

print(longitud([5,5,5]))
#Ejercicio 5

def es_vocal(c:str)->bool:
    resultado = False
    count=0
    for i in c:
        if (c =="a" or c=="e" or c=="i" or c=="o" or c=="u"):
            count = count + 1
        if (count == 1):
            resultado = True
    return(resultado)
        
assert es_vocal ("f") == False
assert es_vocal ("a") == True
assert es_vocal ("ala") == False
assert es_vocal ("aa") == False

print(es_vocal("ii"))

#Ejercicio 6
def intercambiar_dos(s:str)->str:
    s = s.split()
    s1 = s[0]
    s2 = s[1]
    resultado =  s2[:2]+ s1[2:]+" "+ s1[:2]+s2[2:]
    return(resultado)
        
print(intercambiar_dos("esdrujula ambigua"))

#Ejercicio 7
def dar_vuelta(s:str)-> str:
    return (s[::-1])
assert dar_vuelta("hola") == "aloh"

print(dar_vuelta("sinfonica"))

#otra forma

def dar_vuelta2(s:str)->str:
    cadena_nueva = ""
    for i in s:
        cadena_nueva = i + cadena_nueva
    return cadena_nueva
assert dar_vuelta("hola") == "aloh"

print(dar_vuelta2("oyurtsed ol menem"))
#Ejercicio 8
def es_palindromo(s:str)->bool:
    return (s[::-1]==s[0::])
        
            
assert es_palindromo ("radar") == True

print(es_palindromo("anitalavalatina"))

#Ejercicio 9

def superposicion(a:list,b:list)->bool:
    resultado = False
    for i in a:
        for j in b:
            if(i == j):
                resultado = True
                break
            
    return(resultado)
           
assert superposicion([1,2,3],[2,4,8]) == True #(2 si esta en las 2 listas)
assert superposicion([1,3,5],[2,4,6]) == False #(no hay elementos comunes)

print(superposicion([1,2,3],[6,4,8]))  
#Ejercicio 10

def generar_n_caracteres(n:int,c:str)->str:
    return(str(n*c))
assert generar_n_caracteres(5, "x") == "xxxxx"
  
print(generar_n_caracteres(16, "g"))
#Ejercicio 11
def histograma(l:[int])->None:
    for elem in (l):
        print(generar_n_caracteres(elem,"*"))
    
histograma([2,20,40])


