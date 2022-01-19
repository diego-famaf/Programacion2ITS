class MulticonjuntoOrdenado():
    datos = {}
    def __init__(self):
        """
        Inicializacion del Multiconjunto Ordenado
        """
        self.datos = {}
        
        
    def agregar(self, elem):
        """
        Agregar un elemento al multiconjunto
        recuerde que debe quedar en orden
        """
        listOfKeys = self.datos.keys()
        listOfKeys = list(listOfKeys)
        listOfKeys.append(elem) #(agrega e agrega al final)
        
        for indice in range(1,len(self.datos)):
            valorActual = self.datos[indice]
            posicion = indice
            
            while posicion>0 and self.datos[posicion-1]>valorActual:
                self.datos[posicion]=self.datos[posicion-1]
                posicion = posicion-1

            self.datos[posicion] = valorActual
        
        
    def quitar(self, elem):
        """
        Borra una ocurrencia del elemento en el multiconjunto
        """
        self.datos.remove(elem)
        
    def existe(self, elem)->bool:
        """
        Verifica que exista el elemento en el multiconjunto
        """
        return elem in self.datos
        
    def repeticiones_e(self, elem)->int:
        """
        Cantidad de veces repetidas que aparece el elemento e en el multiconjunto
        """
        contador = 0
        for i in self.datos:
            if elem==i:
                contador = contador +1
            
        return contador
    def primero(self):
        """
        Devuelve el primer elemento del multiconjunto
        """
        return (self.datos[0])
    
    def ultimo(self):
        """
        Devuelve el ultimo elemento del multiconjunto
        """
        return (self.datos[len(self.datos)-1])
    
    def devolver_indice(self,elem):
        """
        Devuelve en que orden del multiconjunto se encuentra e
        """
        
        for i in self.datos:
            if i == elem:
                return i
            
        
    def devolver_elemento(self,i:int): 
        """
        Devolveme el elemento que esta en el lugar i
        """
        pass
    def es_vacio(self)->bool:
        """
        Devuelve si el multiconjunto es el vacio
        """
        return self.datos == []
        
    def tamanio(self)->int:
        """
        Devuelve la cantidad de elementos diferentes del multiconjunto
        """
        l = [] # construyo una lista donde esten todos los elementos sin repeticiones
        for i in self.datos:
            if i not in l:
                l.append(i)
        print(l)
        return len(l)
    
    def tamanio_rep(self)->int:
        """
        Devuelve la cantidad de elementos del multiconjunto contando repeticiones
        """
        contador = 0
        for i in self.datos:
              contador = contador + 1
        return contador
    
    def __str__(self):
        """
        Muestra el multiconjunto (hace el print del multiconjunto) (traduccion a string)
        """
        pass
    
    
        
            
        
    
m = MulticonjuntoOrdenado() # m = {}

assert True == m.es_vacio(), "Multiconjunto es vacio"
m.agregar(1) # m = {1}
assert False == m.es_vacio(), "Multiconjunto no es vacio"
assert 1 == m.tamanio(), "Tamanio del multiconjunto es 1"
assert True == m.existe(1), "El elemento 1 existe en el multiconjunto"
assert False == m.existe(-1), "El elemento -1 existe en el multiconjunto"
m.agregar(1) # m = {1,1}
m.agregar(1) # m = {1,1,1}
assert m.tamanio() == 1, "El multiconjunto tiene un elemento"
assert m.tamanio_rep() == 3, "El multiconjunto tiene un elemento"
assert 3 == m.repeticiones_e(1), "Cantidad de repeticiones del elemento 1 es 3"
assert 0 == m.repeticiones_e(20), "Cantidad de repeticiones del elemento 20 es 0"
m.agregar(2) # m = {1,1,1,2}
m.agregar(3) # m = {1,1,1,2,3}
m.agregar(2) # m = {1,1,1,2,2,3}
assert 2 == m.repeticiones_e(2), "Cantidad de repeticiones del elemento 2 es 2"
m.agregar(5) # m = {1,1,1,2,2,3,5}
assert 5 == m.ultimo(), "El ultimo elemento del multiconjunto es 5"
assert 1 == m.primero(), "El primer elemento del multiconjunto es 1"
m.agregar(3) # m = {1,1,1,2,2,3,3,5}
m.quitar(3) # m = {1,1,1,2,2,3,5}
assert True == m.existe(3), "Borramos solo una ocurrenicia de 3"
assert 1 == m.repeticiones_e(3), "Cantidad de repeticiones del elemento 3 es 1"
m.quitar(3) # m = {1,1,1,2,2,5}
assert False == m.existe(3), "No existe el elemento 3"
m.agregar(1) # m = {1,1,1,1,2,2,5}
m.agregar(15) # m = {1,1,1,1,2,2,5,15}
m.agregar(3) # m = {1,1,1,1,2,2,3,5,15}
m.agregar(20) # m = {1,1,1,1,2,2,3,5,15,20}
m.agregar(18) # m = {1,1,1,1,2,2,3,5,15,18,20}
m.agregar(11) # m = {1,1,1,1,2,2,3,5,11,15,18,20}
m.agregar(0) # m = {0,1,1,1,1,2,2,3,5,11,15,18,20}
m.agregar(10) # m = {0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
assert 10 == m.tamanio(), "El multiconjunto tiene 10 elementos distintos"
assert 14 == m.tamanio_rep(), "El multiconjunto tiene 14 elementos contando repeticiones"
assert 5 == m.devolver_indice(10), "El 10 esta en el indice 5"
"""assert 11 == m.devolver_elemento(6), "El elemento del indice 6 es el 11"
m.agregar(-1) # m = {-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-20) # m = {-20,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-3) # m = {-20,-3,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
m.agregar(-3) # m = {-20,-3,-3,-1,0,1,1,1,1,2,2,3,5,10,11, 15,18,20}
assert False == m.existe(22), "No existe el elemento 22"
assert 4 == m.repeticiones_e(1), "Cantidad de repeticiones del 1 es 4"
assert -20 == m.primero(), "El primer elemento del multiconjunto es -20"
assert 20 == m.ultimo(), "El ultimo elemento del multiconjunto es 20"""

