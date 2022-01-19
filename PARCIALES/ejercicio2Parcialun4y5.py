
# Ej 2.a : búsqueda lineal. El código busca de atras para adelante
# El código tiene 2 errores (mínimos), corríjalos para que funcione

def busquedaSecuencial(lista, item)->bool:
    pos = len(lista)-1
    encontrado = False

    while -1 < pos and not encontrado:
        if lista[pos] == item:
            encontrado = True
        else:
            pos = pos-1

    return encontrado

listaPrueba = [1, 2, 32, 8, 17, 19, 42, 13, 33]
assert busquedaSecuencial(listaPrueba, 1) == True
assert busquedaSecuencial(listaPrueba, 33) == True
assert busquedaSecuencial(listaPrueba, 35) == False

print(busquedaSecuencial(listaPrueba,1))
print(busquedaSecuencial(listaPrueba,33))
print(busquedaSecuencial(listaPrueba,35))


