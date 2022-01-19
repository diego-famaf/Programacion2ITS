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
    

print("la poblacion total latinoamericana es de ",poblacion_total(Cantidad_habitantes))

#Problema 4
    
def mismos_elementos(l1:[],l2:[])->bool:
    conjunto1 = set(l1)
    conjunto2 = set(l2)
    
    if (conjunto1==conjunto2):
        return (True)
    else:
        return(False)
    
    
    
    
print(mismos_elementos([1,2,3,4],[4,4,3,3,2,1]))
print(mismos_elementos([1,2,3,4],[4,4,3,3,2]))

#Problema 5

def l1_no_l2(l1:[],l2:[])->set:
    conjunto1 = set(l1)
    conjunto2 = set(l2)
    resultado = (conjunto1 - conjunto2)
    if(conjunto1==resultado):
        return(set())
    else:
        return(resultado)
    
print(l1_no_l2([1,2,3,4],[4,4,3,3,2,1])) #conjunto vacio
print(l1_no_l2([1,2,3,4],[4,4,3,3,2]))   #{1}






