#soloPares

#en haskell:
"""soloPares ::[int]->[int]
   soloPares [] = []
   soloPares (x:xs) | x"mod"2 == 0 = x:soloPares xs
                    | x"mod"2 \= 0 = soloPares xs"""
                 
#python

def soloPares(l:list)->list:
    if l==[]:
        solucion = []
    elif (l[0]%2)==0 :
        solucion = [l[0]] + soloPares(l[1:])
    else:
        solucion = soloPares(l[1:])
    return solucion

print(soloPares([1,2,3,4,5,6]))



        
#duplica el elemento de la lista

#haskell

"""duplica::[int]->[int]
   duplica[] = []
   duplica(x:xs)=(2*x):duplica xs"""

#python

def duplica(a:list)->list:
    if a==[]:
        solucion = []
    else:
        solucion = [2*a[0]] + duplica(a[1:])
        
    return solucion

print(duplica([3,5,7,1,9]))

#todos los elementos de la lista menores a un numero

#haskell

"""todosMenores n ::[int]->Bool
    todosMenores 10 [] = True
    todosMenores 10 (x:xs) | x<10 = todoMenores 10 xs
                           | x>=10 = False"""

#python

def todosMenores (n:int,l:list)->bool:
    if l==[]:
        solucion = True
    elif l[0]<n :
        solucion = todosMenores(n,(l[1:]))
    else:
        solucion = False
    return solucion
        
print(todosMenores(10,([2,6,8,9])))
print(todosMenores(10,([2,6,8,11])))


#dado un numero y una lista,devolver el elemento que esta en la posicion que indica ese numero
#haskell

""" indice ::[a]->int ->a
    indice (x:xs)0 = x
    indice(x:xs)n = indice xs(n-1)"""

# python

def indice(l:list,a:int):
    if a == 0:
        solucion = l[0]
    else:
        solucion = indice(l[1:],a-1)
        
    return solucion

print(indice(["casa",1,"campo",4,"teclado"],3))

#dado un numero y una lista agregar ese numero al final de la lista y devolver la lista resultante

#haskell

"""Pegar::[a]->int->[a]
    Pegar []x = [x]
    Pegar(x:xs)z = x : (Pegar xs z)"""

#python

def pegar(l:list,a:int)->list:
    if l==[]:
        solucion = [a]
    else:
        solucion = [l[0]] + pegar(l[1:],a)
    return solucion

print(pegar([1,"casa","rio"],74))

#concatenar dos listas y devolver la lista resultante

#haskell

"""concatenar::[a]->[a]->[a]
    concatenar []xs = xs
    concatenar (x:xs)ys = x : concatenar xs ys"""

#python

def concatenar(l1:list,l2:list)->list:
    if l2==[] :
        solucion = l1
    elif l1==[]:
        solucion = l2
    else:
        solucion = [l1[0]] + concatenar(l1[1:],l2)
    return solucion

print(concatenar(["sol","singular",2,"mate"],["tango",1,2,3]))

print(concatenar([],["tango",1,2,3]))

        
print(concatenar(["sol","singular",2,"mate"],[]))

#tomar n elementos de una lista y devolver una lista con esos n elementos

#haskell

"""Tomar ::[a] -> Int ->[a]
    Tomar[]n = []
    Tomar xs 0 = []
    Tomar (x:xs)n = x:Tomar xs (n-1)"""

#python

def tomar(l:list,a:int)->list:
    if l==[]:
        solucion = []
    elif a==0:
        solucion = []
    else:
        solucion = [l[0]] + tomar(l[1:],a-1)
    return solucion

print(tomar([1,2,"verde","espacio",9],3))


#sumar 1 a cada numero de una lista y devolver la lista resultante

#haskell

"""sumar1 :: [int]->[int]
        sumar1 [] = []
        sumar1 (x:xs) = (x+1):sumar1 xs"""

#python

def sumar1(l:list)->list:
    if l==[]:
        solucion = []
    else:
        solucion = [l[0]+1] + sumar1(l[1:])
    return solucion

print(sumar1([1,2,9]))

#Dado dos listas ,devolver una lista de tuplas,en donde el primer elemento es de la primer lista y el segundo de la segunda lista,y asi sucesivamente

#haskell

"""repartir :: [string]->[string]->[(string,string)]
   repartir (xs)[] = []
   repartir [](xs) = []
   repartir (x:xs)(y:ys) = (x,y):repartir xs ys"""

#python

def repartir(l1:str,l2:str)->[(str,str)]:
    if l2==[]:
        solucion = l1
    elif l1==[]:
        solucion = l2
    else:
        solucion = [(l1[0],l2[0])] + repartir(l1[1:],l2[1:])
    return solucion

print(repartir(["fit","k","gato"],["delasota","delcaño","spert"]))
print(repartir(["fit","k","gato"],[]))
print(repartir([],["delasota","delcaño","spert"]))

#valor absoluto de una lista de numeros

#haskell

"""absoluto:: [Num]->[Num]
    absoluto[] =[]
    absoluto(x:xs) | x>=0 = x:absoluto xs
                   | x<0  = (-x):absoluto xs"""

#python

def val_absoluto(l:list)->list:
    if l==[]:
        solucion = []
    elif l[0]>=0 :
        solucion = [l[0]] + val_absoluto(l[1:])
    else:
        solucion = [(l[0]*(-1))] + val_absoluto(l[1:])
    return solucion

print(val_absoluto([(-2),(-5),(-9)]))





    

    
    

      
      
    
    


                           
                           
   
    
    
    
