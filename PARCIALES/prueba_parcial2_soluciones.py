# 1 Clases
#a)
"""Crea una clase llamada Cuenta que tendrá los siguientes atributos:
        + titular (que es una persona) y
        + cantidad (puede tener decimales).
    El titular será obligatorio y la cantidad es opcional.
    Construye los siguientes métodos para la clase:
        + Un constructor, donde los datos pueden estar vacíos.
        + Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
    directamente, sólo ingresando o retirando dinero.
        + saldo(): devuelve lo que hay en la cuenta.
        + depositar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa,
    no se hará nada.
        + extraer(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
        + mostrar
"""

class Cuenta:
    def __init__(self,Titular="", cantidad=0):
        self.titular = Titular
        self.dinero = cantidad
    def depositar(self,monto):
        self.dinero += monto
    def extraer(self,monto):
        self.dinero -= monto
    def saldo (self):
        return self.dinero
    def mostrar(self):
        return "Titular: {}, Saldo: {}".format(self.titular,self.dinero)

cuenta = Cuenta ("Juan",0)
cuenta.depositar(2000)
cuenta.extraer(1000)
assert cuenta.saldo() == 1000
cuenta.extraer(2000)
assert cuenta.saldo() == -1000
assert cuenta.mostrar() == "Titular: Juan, Saldo: -1000"

print("Fin ejercicio 1.a!")

#b) 
"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven
que deriva de la anterior. Cuando se crea esta nueva clase guarda la edad del titular.
Construye los siguientes métodos para la clase:
    + Un constructor.
    + Los setters y getters para el nuevo atributo.
    + Método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    + Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    + La cuenta no puede tener saldo negativo.
    + El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir.
"""
class CuentaJoven(Cuenta):
    def __init__(self,Titular="", cantidad=0, edad=18):
        super().__init__(Titular,cantidad)
        self.edad = edad
    def esTitularValido(self):
        return 18 <= self.edad and self.edad < 25
    def extraer(self,monto):
        if self.esTitularValido() and monto <= self.dinero:
            super().extraer(monto)
    def mostrar(self):
        return "Titular: {}, Saldo: {}, Cuenta Joven".format(self.titular,self.dinero)
    

cuenta = CuentaJoven ("Juan",0,23)
cuenta.depositar(2000)
cuenta.extraer(1000)
assert cuenta.saldo() == 1000
cuenta.extraer(2000)
assert cuenta.saldo() == 1000
assert cuenta.mostrar() == "Titular: Juan, Saldo: 1000, Cuenta Joven"
cuenta.esTitularValido() == True

cuenta = CuentaJoven ("Zoe",0,26)
cuenta.depositar(2000)
cuenta.extraer(1000)
assert cuenta.saldo() == 2000
cuenta.esTitularValido() == False

print("Fin ejercicio 1.b!")


# Pilas
class Pila:
    """ Pila es una clase que implemente el tipo abstracto de datos 'pila' del tipo LIFO"""
    """definimos la pila vacia como la lista vacia"""
    def __init__(self):
        self.items = []
    
    def esVacia(self)->bool:
        """pregunta si no hay niongun dato en la pila"""
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

    def tamano(self):
        """me dice al cantidad de elementos que tenemos en la pila"""
        return len(self.items())
    
    def __eq__(self,otra_pila)->bool:
        """Definimos cuando dos pilas son iguales"""
        return (self.items == otra_pila.items)

"""
Escriba una función "palindromo" para manipular palíndromos con espacios.
Por ejemplo, ANITA LAVA LA TINA es un palíndromo que se lee igual hacia
adelante y hacia atrás si se ignoran los espacios en blanco
"""
def palindromo(frase):
    p = Pila()
    for c in frase:
        if c != " ":
            p.incluir(c)
    valor = True
    for c in frase:
        if c != " ":
            valor = valor and (c == p.extraer())
    
    return valor and p.esVacia()

assert palindromo("reconocer") == True
assert palindromo("ANITA LAVA LA TINA") == True

print("Fin ejercicio 2!")

# 3 Colas
"""agregar un método remover que tome un elemento elimine todas las ocurrecias del elemento.
Recuerde utilizar solo los elementos de la pila."""
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
    
    def remover(self,valor):
        for i in range(self.tamanio()):
            a = self.sacar()
            if a != valor:
                self.incluir(a)
    
    
c = Cola()
c.incluir(1)
c.incluir(3)
c.incluir(5)
c.incluir(1)
c.incluir(5)
c.incluir(6)
c.remover(5)
assert c.sacar() == 1
assert c.sacar() == 3
assert c.sacar() == 1
assert c.sacar() == 6

print("Fin ejercicio 3!")

# Matrices
# dada las funciónes
from typing import List,Tuple
Matrix = List[List[int]]

def filas(A:Matrix)->int: #devuelve la cantidad de filas (o m) de la matriz
    return len(A)

def columnas(A:Matrix)->int: #devuelve la cantidad de columnas (o n) de una matriz
    return len(A[0])

def dimension(A:Matrix)->Tuple[int,int]: # Devuelve 
    return (filas(A),columnas(A))


"""Escriba una función que tome una matriz cuadrada (n y m son iguales) y
devuelva
+ una lista con la diagonal de esa matriz (la diagonal es cuando
recorro la matriz e i==j) 
+ otra que sume los elementos de esa lista. """
c = [[1,3,5],
     [4,3,5],
     [2,1,2]] # 3 filas x 3 columnas

def diag (M:Matrix)->List[int]: #
    (n_filas,n_columnas) = dimension(M)
    lista = []
    if n_filas == n_columnas:
        for i in range (n_filas):
            lista.append(M[i][i])
    return lista

def sum_diag(M:Matrix)->int:
    sum = 0
    for i in diag(M):
        sum = sum + i
    return sum

assert diag (c) == [1,3,2]
assert sum_diag (c) == 6

print("Fin ejercicio 4!")

