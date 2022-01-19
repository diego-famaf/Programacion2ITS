#problema 1

guardar = input("Ingrese  un día de la semana:")

if(guardar=="lunes"or guardar=="martes" or guardar=="miercoles"):
    print("comienza la semana")
elif(guardar=="jueves" or guardar=="viernes"):
    print("termina la semana")
elif(guardar=="sabado" or guardar=="domingo"):
    print("estoy descansando")
else:
    print("no ingreso un dia de la semana,intentelo otra vez")
    
    
#problema 2
    
poblacion = {"Brasil": 210147125,
             "Colombia": 50372424,
             "Argentina" :44938711}
       
    
def valor_promedio(d:dict)->int:
    total = 0
    for i in d:
        total = total + int(d[i])
    promedio= total/len(d)
    return(promedio)    


assert valor_promedio(poblacion) == 101819420   

print(valor_promedio(poblacion))
#problema 3

#Escriba un programa que tome 3 valores y diga si 'A es mayor a B y 'B es mayor a C o C mayor a B'

def f(a:int,b:int,c:int):
    resultado = False
    if a>b and b<c:
        resultado = True
    return(resultado)
        
    
assert f(3,1,2) == True
assert f(3,1,1) == False
assert f(1,3,4) == False

print(f(5,4,7))

#problema 4

#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí

#DIGA sí PARA CONTINUAR
#¿Desea continuar el programa?: sí
#¿Desea continuar el programa?: sí
#¿Desea continuar el programa?: NO
#¡Hasta la vista!


while True:
    respuesta = input("Desea continuar?:")
    if respuesta != "si":
        break
    
print ("Hasta la vista")



#problema 5

#Escribir una función que tome una lsita y un valor y elimine todas las ocurrencias del valor en la lista

def remover_valor(l:list,v)->list:
    
    r = l
    for i in l:
        if (i == v):
            l.remove(i)
            
        
    return r

assert remover_valor([1,2,3,1,2,3],3) == [1,2,1,2]
            


print(remover_valor([2,3,3,3,3,3],3))


