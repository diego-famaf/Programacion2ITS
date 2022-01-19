#Busqueda binaria

def busquedaBinaria(unaLista, item):
    if len(unaLista) == 0:
        return False

    else:
        puntoMedio = len(unaLista)//2
        if unaLista[puntoMedio]==item:
            return True
        else:
            if item < unaLista[puntoMedio]:
                return busquedaBinaria(unaLista[:puntoMedio],item)
            else:
                return busquedaBinaria(unaLista[puntoMedio+1:],item)

listaPrueba = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print(busquedaBinaria(listaPrueba, 12))
print(busquedaBinaria(listaPrueba, 16))

