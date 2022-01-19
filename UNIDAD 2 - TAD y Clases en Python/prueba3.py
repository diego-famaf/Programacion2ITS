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


#Crear una clase circulo: 
#constructor: punto(x, y), radio; 
#operaciones:diametro,  perimetro y area.

#Tomar de ejemplo la clase rectangulo
class Circulo:
    radio = 0
    centro = Punto()
    
    
    def __init__( self,radio,x=0,y=0 ): # toma un radio , centro
        
        self.radio = radio
        
    def diametro ( self ):
        return (2*self.radio)
    def perimetro_circulo ( self ):
        return (2 * 3.141592653589793 * self.radio)
    def area_circulo ( self ):
        return (3.141592653589793 * (self.radio)**2)
    def __eq__(self,otro):
        return ((self.radio == otro.radio))
        pass
    def mover(self):
        pass
c = Circulo(4.5, 0, 0)
assert c.diametro() == 9.0
assert c.area_circulo() == 63.61725123519331
assert c.perimetro_circulo() == 28.274333882308138

class Fraccion:
    
    def __init__(self,arriba,abajo):
       #inicializa una variable del tipo fraccion
        self.num = arriba # Numerador
        self.den = abajo # Denominador
    def __str__(self):
        #Convertir el objeto en cadena para poder imprimirlo”””
        return ("{} {} {}".format(self.num, "/", self.den))
        
        
    def __add__(self, otraFrac):
        
        num = self.num + otraFrac.num
        den = self.den + otraFrac.den
        
        resultado = Fraccion(num,den)
        return resultado
    
        #Sumar dos fracciones y retornar resultado, pueden tener distinto denominador”””
        
    def __eq__(self, otraFrac):
        
        return (self.num / self.den) == (otraFrac.num / otraFrac.den) 
       #compara dos fracciones y dice si son equivalentes”””
        

q = Fraccion(2,4)
p = Fraccion(1,2)
r = Fraccion(2,3)
print(q)
c =q.__add__(p)
print(c)

f =q.__eq__(p)
print(f)

g=q.__eq__(r)
print(g)


# q == p ?

