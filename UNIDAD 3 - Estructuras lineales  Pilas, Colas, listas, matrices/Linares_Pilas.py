class Pila:
    """ Pila es una clase que implemente el tipo abstracto de datos 'pila' del tipo LIFO"""
    """definimos la pila vacia como la lista vacia"""
    
    
    def __init__(self):
        self.items = []
        
    def esVacia(self)->bool:
        """pregunta si no hay ningun dato en la pila"""
        #return len(self.items) == 0
        return self.items == [] 

    def incluir(self, item)->None:
        """agrega un elemento a mi pila"""
        self.items.append(item)

    def extraer(self):
        """extrae un elemento de la pila, en este caso el último de la lista"""
        return self.items.pop() # me devuelve el ultimo elemento y lo borra

    def inspeccionar(self):
        """Ver cual es el tope de la pila"""
        return self.items[-1]

    def tamaño(self):
        """me dice al cantidad de elementos que tenemos en la pila"""
        return len(self.items)
    
    def __eq__(self,otra_pila)->bool:
        """Definimos cuando dos pilas son iguales"""
        return (self.items == otra_pila.items)
    
    def dar_vuelta(self):
        elementos = [] #creo una lsita vacia
        while not self.esVacia(): #mientras la pila no este vacia
            elementos.append(self.extraer()) # extraigo el ultimo elemento y lo pongo en una lista
        for elemento in elementos: # recorro los elementos de la lista
            self.incluir(elemento)
            
    def imprimir_pila(self):
        for i in self.items:
            print(i)
            
    def vaciar_pila(self):
        if not self.esVacia():
            return self.items.clear()
                
            

p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
print(p.tamaño())
print(p.items)
assert p.inspeccionar() == 1
assert p.items == [4, 2, 1]
p.dar_vuelta()
#assert p.extraer() == 1
#assert p.inspeccionar() == 2
#print (p.inspeccionar())
print(p.items)
p.imprimir_pila()
p.vaciar_pila()
assert p.esVacia() == True
print(p.items)
p.incluir(8)
p.incluir(2)
p.incluir(10)
print(p.items)
p.extraer()
assert p.extraer() == 2
print(p.items)

p.vaciar_pila()
assert p.esVacia() == True
print(p.items)

#3
def revertir(c:str):
    
    if c!="":
        d=c.split()# covierto una cadena en lista
        elementos =[]
        for i in range(len(d)):
        
            elementos.append(d.pop()) # mientras recorro los elementos de la lista d voy agregando a la lista vacia "elementos",el ultimo elemento que va quedando 
        resultado = " ".join(elementos)
        print(resultado)
    


revertir("Mi Diario Python algo 4 tango")



#4

def contar0y1(palabra:str)->bool:
    pila0 = Pila()
    pila1 = Pila()
    
    
    contador0=0
    contador1=0
    for i in palabra:
        if i == "0":
            
            pila0.incluir(0)
            contador0+=1
            pila0.vaciar_pila()
        if i == "1":
            
            pila1.incluir(1)
            contador1+=1
            pila1.vaciar_pila()
           
    return contador0 == contador1
     
    
assert contar0y1("a01") == True


assert contar0y1("a011") == False
 
print (contar0y1("a000011"))
print(contar0y1("a010101"))

#4 otra version

def vcontar0y1(palabra:str)->bool:
    pila0 = Pila()
    pila1 = Pila()
    
    for i in palabra:
        if i == "0":
            pila0.incluir(0)
        if i == "1":
            pila1.incluir(1)
            
    return pila0.tamaño()==pila1.tamaño()

assert vcontar0y1("a01") == True
assert vcontar0y1("a011") == False
 
print (vcontar0y1("a000011"))
print(vcontar0y1("a010101"))

#5
def balanceada(expresion:str)->bool:

    pila0 = Pila()
    pila1 = Pila()
    
    for i in expresion:
        if i == "(":
            pila0.incluir(i)
        if i == ")":
            pila1.incluir(i)
            
    return pila0.tamaño()==pila1.tamaño()



assert balanceada("()()()") == True
assert balanceada("()()())") == False


print(balanceada("()()()"))
print(balanceada("(()()()"))

#6

"""def  balanceada_general(expresion:str)->bool:
    
    pila_posicion = Pila()
    pila_posicion_sig = Pila()
    
    
    
    
    if "(" in expresion :
        pila_posicion.incluir(expresion.index("("))
        pila1 = pila_posicion.extraer()
    if ")" in expresion:
        pila_posicion_sig.incluir(expresion.index(")"))
        pila2 = pila_posicion_sig.extraer()
        
        resultado = pila1==pila2-1
    
    if "[" in expresion:
        pila_posicion.incluir(expresion.index("["))
        pila3 = pila_posicion.extraer()
        
    if "]" in expresion:
        pila_posicion_sig.incluir(expresion.index("]"))
        pila4 = pila_posicion_sig.extraer()    
        resultado = pila3 == pila4-1
    
    
    
    if "{" in expresion:
        pila_posicion.incluir(expresion.index("{"))
        pila5 = pila_posicion.extraer()
        
    if "}" in expresion:
        pila_posicion_sig.incluir(expresion.index("}"))
        pila6 = pila_posicion_sig.extraer()    
        resultado = pila5 == pila6-1
    
    
    return resultado

        
        
                                                     
        
       
 #comparar con la posicion


assert balanceada_general("()[]") == True

assert balanceada_general("[](()[)]") == False"""

#6 version que si funciona

def balanceada_general2(expresion:str)->bool:
    pila=Pila()
    parentesis = {"{":"}","(":")","[":"]"}# clave:valor,como diccionario ,para que en el if dentro del for me encuentre solo las claves
    
    for c in expresion:#recorro el string iterando con c
        if c in parentesis:#me fijo si el elemento esta como clave en el diccionario parentesis
            pila.incluir(c)# si esta lo agrego a la pila,porque solo esoy buscando los elementos que abren
             
        elif pila.tamaño() == 0 or c!= parentesis[pila.extraer()] :#en cambio,si no hay elementos en la pila o no es un elemento de cierre igual que el que esta en la pila
            return False# quiere decir que no es valido
    return pila.tamaño()==0

assert balanceada_general2("()[]") == True

assert balanceada_general2("({)") == False

print(balanceada_general2("()[]"))
print(balanceada_general2("()[]}{}"))

#7
def capicua(palabra:str)->bool:
    palabra = palabra.lower()
    
    pila1=Pila()
    pila2=Pila()
    pila3=Pila()
     
    
    
    for i in palabra:
        pila3.incluir(i)
    
    for i in palabra:
        
        pila1.incluir(i)
        
    while not pila1.esVacia():
        pila2.incluir(pila1.extraer())
    
    
    return pila2.__eq__(pila3)
    
    
assert capicua("AbebA") == True

assert capicua("Abe") == False


print(capicua("AbebA"))
print(capicua("Abe"))

#8

class Pila2:
    
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, item)->None:
        self.items.insert(0,item)
        
    ## Completar aca ##

    def extraer(self):
        return self.items.pop(0)
        
    ## Completar aca ##

    def inspeccionar(self):
        return self.items[0]

    def tamano(self):
        return len(self.items)
    

h = Pila2()

h.incluir(0)
h.incluir(2)
h.incluir(3)


print(h.items)

h.extraer()

print(h.items)


