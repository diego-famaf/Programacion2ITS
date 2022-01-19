#Problema 1

Tupla1 = (4,True,"cinco")
Tupla2 = ("Argentina","Peru",1,2)
Tupla3 = (False,3,2.4)

print(Tupla1,Tupla2,Tupla3)

#Problema 2

def max_min(l:[])->tuple:
    maximo = l[0]
    minimo = l[0]
    for i in l:
        if (i>maximo):
            maximo = i
        
        if (i<minimo):
            minimo = i
    resultado=(maximo,minimo)    
    return(resultado)
    
print(max_min([48,-2,10]))

#Problema 3
Cantidad_habitantes = {"Brasil":"210147125","Colombia":"50372424","Argentina":"44938712","Perú":"32131400",
                       "Venezuela":"28670000","Chile":"19107216","Ecuador":"17300000","Bolivia":"11383940",
                       "Paraguay":"7152703","Uruguay":"3529140","Guyana":"761000","Surinam":"524000",
                       "Guayana Francesa":"187000"}

for i in Cantidad_habitantes:
    print(Cantidad_habitantes[i],"es el numero de habitantes de",i)
    
def poblacion_total(Cantidad_habitantes):
    resultado = 0
    for i in Cantidad_habitantes:
        resultado = resultado + int(Cantidad_habitantes[i])
    return(resultado)    
    

print(poblacion_total(Cantidad_habitantes))


    


# max_min([3,-1,6,22]) == (22,-1)
# max_min([3,6,22]) == (22,3)


