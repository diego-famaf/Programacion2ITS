#busqueda secuencial

def busquedaSecuencialOrdenada(unaLista, item):
    pos = 0
    encontrado = False
    parar = False
    while pos < len(unaLista) and not encontrado and not parar:
        if unaLista[pos] == item:
            encontrado = True
        else:
            if unaLista[pos] > item:
                parar = True
            else:
                pos = pos+1

    return encontrado

listaPrueba =  [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
"print(busquedaSecuencialOrdenada(listaPrueba, 12))"
print(busquedaSecuencialOrdenada(listaPrueba, 16))