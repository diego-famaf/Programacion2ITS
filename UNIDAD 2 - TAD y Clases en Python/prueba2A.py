class Punto:
    """Un punto en el espacio bi dimensional:
    - coordenada x
    - coordenada y
    """
    x = 0
    y = 0

    def __init__(self, x=0, y=0): # si no paso x e y se considera que el punto es (0,0) 
        self.x = x
        self.y = y

    def __eq__(self, otro)->bool:
        """Devolver True si self es igual a otro."""
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return "Punto: ({},{})".format(self.x, self.y)
    
    def es_origen(self)->bool:
        """Me dice si el punto corresponde al origen del plano"""
        return (self.x ==0 and self.y ==0)
    
    def mover(self,dx,dy): # (1,2) moverlo 2 a la dercha y uno arriba -> (1+2,2+1)
        """Mueve el punto dx lugares en x y dy lugares en y"""
        # (1,2) moverlo 2 a la dercha y uno arriba -> (1+2,2+1)
        # (1,2) moverlo 2 a la izquierda y uno abajo -> (1-2,2-1)
        self.x = self.x + dx # muevo dx puntos en el eje x
        self.y = self.y + dy # muevo dy puntos en el eje y
    
    def distancia(self,otro):
        # pitagoras -> a**2 + b**2 = h**2
        return ((self.x-otro.x)**2 + (self.y-otro.y)**2)**1/2
    
    def distancia_origen(self,x,y):
        return ((self.x)**2 + (self.y)**2)**(1/2)

a = Punto(1,2)
print(a)
a.mover(5,3)
print(a)
print(a.es_origen())
b = Punto()
print(b.es_origen())
c = Punto(6,5)
print(c)

print (b==c) # Falso
print (a==c) # True

origen = Punto()
b.distancia(c)


k = Punto(5,5)
p= Punto(1,5)
print(b.distancia(c))
print(k)
print(k.distancia_origen(5,5))
print(p.distancia_origen(1,5))

#2B

#
def mas_lejos(lista:[Punto]):
     #toma una lista de puntos y devuelve el mas alejado del origen
        # mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)]) == Punto(5,5)
        
     
    j = Punto()
    
    for i in range(len(lista)-1): 
        if(distancia_origen() > j.distancia_origen(lista[i+1],)):
            j=Punto(lista[i])
        
            
    return (j)                       

mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)])

