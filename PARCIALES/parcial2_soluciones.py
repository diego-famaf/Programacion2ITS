# 1 Clases
"""
Crea una clase llamada Polígono que tendrá los siguientes atributos: 
    + número de lados (un entero)
    + origen (un punto x,y en el plano)
    Tanto el numero de lados como el origen son obligatorios
    Construye los siguientes métodos para la clase:
    + Un constructor, donde los datos pueden estar vacíos.
    + Es válido. (los polígonos deben tener más de 2 lados)
    + Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
    Además:
    + mover (básicamente es actualizar el atributo origen)
    + __str__ describe el polígono con sus atributos
 """

class Poligono():
    def __init__(self,lados,origen):
        self.lados = lados
        self.origen = origen
    def obtener_lados(self):
        return self.lados
    def obtener_origen(self):
        return self.origen
    def modificar_lados(self,lados):
        self.lados=lados
    def modificar_origen(self,origen):
        self.origen=origen
    def mover(self,origen):
        self.origen=origen
    def __str__(self):
        return "Polígono, lados: {}, origen {}".format(self.lados,self.origen)
    def es_valido(self):
        return self.lados > 2
    
poligono = Poligono (3,(0,0))
assert poligono.es_valido() == True
assert poligono.obtener_origen() == (0,0)
poligono.mover((0,1))
assert poligono.obtener_origen() == (0,1)
assert poligono.__str__() == "Polígono, lados: 3, origen (0, 1)"

poligono = Poligono (2,(0,0))
poligono.es_valido() == False

print("Fin ejercicio 1.a!")
# 1.b
"""
Extienda la clase polígono utilizando herencia para crear otra llamada Polígono regular que represente esta figura
    + deberá agregar como atributo la longitud de los lados, con sus getters y setters
    + modifique el init para incluir el largo de lados
    Agregar como métodos
    + como es un poligono regular sabemos que "angulo = 360°/cantidad de lados". Implemente un método que lo calcule
    + calcular el perímetro del polígono
    + modifique el método str para indicar que es un polígono regular y la longitud de sus lados
"""    
class Poligono_regular(Poligono):
    def __init__(self,lados,origen,largo = 1):
        super().__init__(lados,origen)
        self.largo = largo
    def angulo(self):
        return 360/self.lados
    def perimetro(self):
        return self.lados*self.longitud
    def __str__(self):
        return "Polígono Regular, lados: {}, origen {}, largo lados: {}".format(self.lados,self.origen,self.largo)
 
poligono = Poligono_regular (3,(0,0),2)
assert poligono.obtener_origen() == (0,0)
poligono.mover((0,1))
assert poligono.obtener_origen() == (0,1)
assert poligono.angulo() == 120
poligono.perimetro = 6
print (poligono)
assert poligono.__str__() == "Polígono Regular, lados: 3, origen (0, 1), largo lados: 2"

poligono = Poligono_regular (2,(0,0))
poligono.es_valido() == False

print("Fin ejercicio 1.b!")

# 2 Pilas
class Pila:
    def __init__(self):
        self.items = []
    
    def esVacia(self)->bool:
        """pregunta si no hay niongun dato en la pila"""
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

    def tamano(self):
        """me dice al cantidad de elementos que tenemos en la pila"""
        return len(self.items())
    
    def __eq__(self,otra_pila)->bool:
        """Definimos cuando dos pilas son iguales"""
        return (self.items == otra_pila.items)
    
    def __str__(self):
        return str(self.items)
    
    def remover(self,item):
        for v in self.items:
            if v==item:
                self.items.remove(v)
    def montar(self,otra_pila):
        self.items = self.items + otra_pila.items
        
    

"""
Agregue 2 métodos:
a) remover: pila x tipo_item -> pila: elimina todas las ocurrencias de un item en la pila 
b) montar: pila x pila  →  pila,  para  poner  la  segunda  pila  encima  de  la  primera
(respetando el orden de los elementos).
"""

p = Pila()
p.incluir(1)
p.incluir(3)
p.incluir(5)
p.incluir(1)
p.incluir(5)
p.incluir(6)
p.remover(5)

assert p.extraer() == 6
assert p.extraer() == 1
assert p.extraer() == 3
assert p.extraer() == 1

print("Fin ejercicio 2.a!")

p1 = Pila()
p1.incluir(1)
p1.incluir(3)
p1.incluir(5)

p2 = Pila()
p2.incluir(1)
p2.incluir(5)
p2.incluir(6)

p1.montar(p2)
assert p1.__str__() == "[1, 3, 5, 1, 5, 6]"

print("Fin ejercicio 2.b!")

# 3 Colas
class Cola:
    """La cola es una coleccion de datos lineales, FIFO (First in First out)"""
    def __init__(self):
      self.elementos = []
      
    def incluir(self, item):
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
    
    def mezclar(self,c2):
        c = []
        i = 0
        len_c1 = len(self.elementos)
        len_c2 = len(c2.elementos)
        iter = max(len_c1,len_c2)
        for i in range (iter):
            if i<len_c1:
                c.append(self.elementos[i])
            if i<len_c2:
                c.append(c2.elementos[i])
        self.elementos = c
    
"""
Agregue 1 métodos:
+ mezclar: mezclar alternativamente los elementos de dos colas (no tienen que 
ser necesariamente de la misma longitud)
"""

c = Cola()
c.incluir(1)
c.incluir(3)
c.incluir(1)
c.incluir(5)

c2 = Cola()
c2.incluir(1)
c2.incluir(5)
c2.incluir(6)
c.mezclar(c2)
assert c.__str__() == "[1, 1, 3, 5, 1, 6, 5]"

print("Fin ejercicio 3!")

# 4 Matrices
# dada las funciónes
from typing import List,Tuple
Matrix = List[List[int]]

def filas(A:Matrix)->int: #devuelve la cantidad de filas (o m) de la matriz
    return len(A)

def columnas(A:Matrix)->int: #devuelve la cantidad de columnas (o n) de una matriz
    return len(A[0])

def dimension(A:Matrix)->Tuple[int,int]: # Devuelve una tupla (un par) con el valor (filas,columnas)
    return (filas(A),columnas(A))

"""
Las matrices simétricas son matrices donde para todo elemento de la matriz a[i][j] == a [j][i],
fíjense que esto funciona si la matriz es cuadrada, filas(M) = columna(M)
Escriba una función que tome una matriz cuadrada (n y m son iguales) y
devuelva si es simétrica o no.
"""
M1 = [[1,3,5],
      [4,3,5],
      [2,1,2]] # 3 filas x 3 columnas

M2 = [[1,2,3],
      [2,3,5],
      [3,5,2]] # 3 filas x 3 columnas

def matriz_simetrica(M:Matrix)->bool:
    valor = True
    for i in range(filas(M)):
        for j in range(columnas(M)):
            valor = valor and (M[i][j]==M[j][i])
    return valor

assert matriz_simetrica(M1) == False
assert matriz_simetrica(M2) == True

print("Fin ejercicio 4!")