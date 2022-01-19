class Poligono():
    
    x=0
    y=0
    
    def __init__(self,lados=0,origen=(x,y)):
        self.lados=lados
        self.origen = origen
        
        
    def es_valido(self):
        return self.lados>2
    
    def mover(self,dx, dy): 
        self.x = self.x + dx # muevo dx puntos en el eje x
        self.y = self.y + dy # muevo dy puntos en el eje y
    
    def __str__(self):
        return "Poligono:lados: {}, origen: {}".format(self.lados,self.origen)
    
    def obtener_origen(self):
        return self.origen
    
    
poligono = Poligono (3,(0,0))
poligono.es_valido() == True
poligono.obtener_origen() == (0,0)

poligono.mover(0,1)
poligono.obtener_origen() == (0,1)

poligono.__str__() == "Polígono, lados: 3, origen (0,1)"

poligono = Poligono (2,(0,0))
poligono.es_valido() == False

print(poligono)

class Poligono_regular():
    x=0
    y=0
    
    def __init__(self,lados=0,origen=(x,y),largo=0):
        super().__init__(lados,origen)
        self.largo = largo
    
    def angulo(self):
        return 360/len(lados)
    
    def perimetro():
        return len(lados)*largo
    
    
    def __str__(self):
        return "Poligono Regular:lados: {}, origen: {},largo lados: {}".format(self.lados,self.origen,self.largo)
    
    
    
    
poligono = Poligono_regular (3,(0,0),2)
poligono.obtener_origen() == (0,0)
poligono.mover((0,1))
poligono.obtener_origen() == (0,1)
poligono.angulo() == 120
poligono.perimetro = 6
poligono.__str__() == "Polígono Regular, lados: 3, origen (0,0), largo lados: 2"

poligono = Poligono_regular (2,(0,0))
poligono.es_valido() == False

print("Fin ejercicio 1.b!")    
    