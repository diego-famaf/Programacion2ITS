#Colas

#Ejercicicio 3: Implementar en un archivo de python la clase cola vista en clase
class Cola:
    """La cola es una coleccion de datos lineales, FIFO (First in First out)"""
    def __init__(self):
        self.elementos = []
      
    def agregar(self, item):
        self.elementos.append(item)

    def es_vacia(self)->bool: 
        return self.elementos == []

    def primero(self): # fijarse que no este vacia
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
    def __str__(self):
        return ("{}".format(self.elementos))
    
    def imprimir_cola(self):
        for i in self.elementos:
            print(i)
            
    def vaciar(self):
        if not self.es_vacia():
            return self.elementos.clear()
        
    def dar_vuelta(self):
        elementos2 = [] #creo una lsita vacia
        while not self.es_vacia(): #mientras la cola no este vacia
            elementos2.append(self.elementos.pop()) # extraigo el primer elemento y lo pongo en una lista
        print(elementos2)
        for elemento in elementos2: # recorro los elementos de la lista
            self.agregar(elemento)
        

p = Cola() # crea una cola (vacia)
print(p.es_vacia()) #True
p.agregar(4) # 
p.agregar('perro')
print(p.elementos) # [4,'perro']
print(p.primero()) # 4
p.agregar(True) # [4,'perro',true]
p.dar_vuelta()
print(p)
print(p.tamanio()) # 3
print(p.es_vacia()) #False
p.agregar(8.4) # [4,'perro',true,8.4]
print(p.sacar()) # imprime el 4 y lo saca
print(p.sacar()) # impreme perro y lo saca
print(p.tamanio()) # 2


# Ejercicio 4: 
# Agregar a la clase cola los siguientes métodos (usando preferentemente los métodos ya utilizados)
#    1. Imprimir cola
#    2. Vaciar la cola.
#    3. Dar vuelta cola

# Ejercicio 5:
# Escriba una función que reciba una Cola C1 y mueva sus elementos a una nueva Cola c2,
# manteniendo el orden de salida de los elementos. Al finalizar la Cola C1 no debe contener elementos.

def trasladar(c1:Cola)->Cola:
    resultado = Cola()
    while not (c1.es_vacia()):
        resultado.agregar(c1.sacar())
        
    return resultado   
    
c1=Cola()
p.agregar(4)
p.agregar(5)
p.agregar(6)
c3 = trasladar(p)
assert c1.es_vacia() == True

print(c3)

"""#5 bis
def trasladar2(c:Cola)->Cola:
    c1= Cola()
    resultado = Cola()
    for i in range (c.tamanio()):
        valor = c.sacar() #quita el primer elemento de la cola,lo devuelve y lo elimina de la cola
        resultado.agregar(valor)
        
    
    return resultado

c = Cola()


c2 = trasladar2(["1","2","3"])
assert c.es_vacia() == True"""

#6

def concat(c1:Cola,c2:Cola)->Cola: # resultado = C1+C2
    resultado = Cola()
    for i in range (c1.tamanio()):
        valor = c1.sacar()
        resultado.agregar(valor)
        c1.agregar(valor)
    for i in range (c2.tamanio()):
        valor = c2.sacar()
        resultado.agregar(valor)
        c2.agregar(valor)
    return resultado

c1 = Cola()
print(c1)
c1.agregar(1)
c1.agregar(4)
c1.agregar(8)
c2 = Cola()
c2.agregar(4)
c2.agregar(2)
c2.agregar(7)
print(c1)
print(c2)

res = concat(c1,c2)
print (res)

# Ejercicio 7
"""Escriba una rutina que reciba dos Colas C1 y C2 de números enteros y 
proceda a intercambiar sus elementos, manteniendo el orden de salida de los mismos.
 Al finalizar la rutina, la Cola C1 tendrá los elementos de la 
Cola C2 y ésta a su vez tendrá los elementos de la Cola C1."""

#mi idea aca es usar una cola c3 para pasar c1,quedando c1 vacia,despues pasar c2 a c1,quedando c2 vacia,y finalmente
#pasar c3 a c2,quedando c3 vacia.
def intercambiar(c1:Cola,c2:Cola)->Cola:
    
    resultado = Cola()
    for i in range (c1.tamanio()):
        valor = c1.sacar()
        resultado.agregar(valor)
        c3.agregar(valor)
    for i in range (c2.tamanio()):
        valor = c2.sacar()
        resultado.agregar(valor)
        c1.agregar(valor)
    for i in range (c3.tamanio()):
        valor = c3.sacar()
        resultado.agregar(valor)
        c2.agregar(valor)
        
    return resultado
            
    
c2 = Cola()
c1 = Cola()
c3=Cola()
c1.agregar(6)
c1.agregar(9)
c1.agregar(2)
print(c1)
c2.agregar(4)
c2.agregar(5)
c2.agregar(6)
print(c2)
intercambiar(c1,c2)

print(c1)
print(c2)


#8
#De una lista de ejemplos de problemas donde puede
#usarse una cola como sistema de administración de
#la información y como podría pensarse un programa pensando estas ideas.

#La cola de atencion en un banco,se podria usar un programa usando colas para controlar cuantos clientes se van juntando en la cola de espera dependiendo
#del tiempo que demoran en irse los clientes que van siendo atendidos,y filtrando quizas por el tipo de tramite se podria
#derivar los clientes a otras colas para agilizar la atencion


#en una cola de atencion de despacho de productos del correo,para ver cuanto tiempo tarda en irse alguien con su encomienda
#y ser atendido la siguiente persona en la cola,como una estadistica para implementar sistemas de ingreso y egreso de la cola
#mas dinamico

# La cola que se puede formar en una atencion medica de urgencia,se podria usar un programa para analizar si conviene mas dar un tiket de espera para que las personas
#sean desencoladas rapidamente y no tener gran acumulacion de personas en una fila.