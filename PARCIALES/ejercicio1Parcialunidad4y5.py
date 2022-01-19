# Ej 1: Recursion: Defina una función para contar la cantidad de espacios que hay en una oracion

def espacios(frase:str)->int:
    if frase == "":  #si la oracion esta vacia
        solucion = 0
    elif frase[0] == " ": #Si hay un espacio al comienzo
        solucion = 1 + espacios(frase[1:])
    else:
        solucion = espacios(frase[1:])
    return solucion

assert espacios ("") == 0
assert espacios ("La casa de al lado") == 4


#pista: la frase puede estar vacia, puede empezar con un espacio, o empezar con algo que no sea espacio

"""def espacios(frase:str)->int:
    contador = 0
    if frase=="":
        contador = 0
    elif (frase[0] == "")and (frase[1:]!=""):
        contador = 1
    elif (frase == frase+""+frase):
        contador = 1 + espacios(frase[1:])
    else:
        contador= espacios(frase[1:])
    return contador
    

assert espacios ("") == 0
assert espacios ("La casa de al lado") == 4"""
