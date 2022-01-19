class RegistroAlumnoMateria:
    
    def __init__(self,nombre,materia):# Agregar parámetros
        self.nombre = nombre
        self.materia = materia
        self.notas = []
        self.nota = 0
        
    #¨¨¨funcion que inicializa una variable registroAlumnoMateria¨¨¨

    def __str__(self):
        return ("{} {} {}".format(self.nombre, self.materia, self.notas))

    def mostrar_estado(self):
        
        resultado =""
        if(self.calcular_promedio() < 4):
            resultado = "libre"
            
        elif(self.calcular_promedio() >= 7 ):
            resultado ="promocionado"
        else:
            resultado ="regular"
        return resultado
        
    #¨¨¨calcula si esta regular, promocionado, o libre¨¨¨

    def agregar_nota(self,nota):
        self.notas.append(nota)
         
        
        
    def mostrar_notas(self):
        return ("{}".format(self.notas))
        
        

    def calcular_promedio(self):
        suma=0
        for i in self.notas:
            suma += i
        
        return (suma/len(self.notas))
    
        
        
k = RegistroAlumnoMateria("Diego", "Biologia")
k.agregar_nota(10)
k.agregar_nota(5)
k.agregar_nota(6)


print(k)
print(k.mostrar_notas())
print(k.calcular_promedio())
print(k.mostrar_estado())


