#quick_short

a=[]
primera pasada()
pivot =


#incertion
a=[]
1)           i=0
2)           i=1
3)           i=2
4)

#busqueda binaria iterativa(la lista tiene que estar ordenada)
# Ej 3 : búsqueda binaria (iterativa)
#a. indique la secuencia de busqueda binaria iterativa para 10 , ¿Cuantas comparaciones hace?
#b. indique la secuencia de busqueda binaria iterativa para 8 , ¿Cuantas comparaciones hace?

a = [1, 3, 5, 5, 7, 9, 10, 12, 13, 16]
     0  1  2  3  4  5  6   7   8   9
primero=0
ultimo=9
medio=primero+ultimo//2 = 4 ->7
primero =4
ultimo =9
medio=primero+ultimo//2 =6 ->10
#numero de comparaciones = 2

primero=0
ultimo=9
medio=primero+ultimo//2 = 4 ->7
primero=4
ultimo=9
medio=primero+ultimo//2 = 6 ->10
primero=5
ultimo=6
medio=primero+ultimo//2 = 5 ->9
primero=5
ultimo=5
medio=primero+ultimo//2 = 0 ->1
resultado = false
#numero de comparaciones = 4

--------------------------------------------
# Ej 4: Ordenamiento por inserción
# Muestre como cambia el orden de la lista despues de 5 pasadas (debera mostrar el resultado para la pasada 1, pasada 2, etc.
a = [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]



#incertion
a = [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]
1) [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]          i=0
2) [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]          i=1
3) [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]          i=2
4) [5, 9, 16, 12, 1, 10, 5, 13, 7, 3]          i=3
5) [5, 9, 12, 16, 1, 10, 5, 13, 7, 3]          i=4



------------------------------------

# Ej 5: Ordenamiento rápido
# Muestre como cambia el orden de la lista despues de 5 pasadas del quicksort,debera mostrar el resultado para la pasada 1, pasada 2, etc.
a = [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]


#quick_short

a = [9, 16, 5, 12, 1, 10, 5, 13, 7, 3]
primera pasada(0,9)
pivot = 9

1) [9, 16i, 5, 12, 1, 10, 5, 13, 7, 3d] 16<9 ?no,paro ,3>9?no ,paro
2) [9, 3i, 5, 12, 1, 10, 5, 13, 7, 16d]   intercambio
3) [9, 3, 5, 12i, 1, 10, 5, 13, 7d, 16]3<9? si,sigo;5<9?si,sigo;12<9?no,paro;   16>9?si,retrocedo1 ;7>9?no,paro
4) [9, 3, 5, 7i, 1, 10, 5, 13, 12d, 16] intercambio
5) [9, 3, 5, 7, 1, 10i, 5d, 13, 12, 16]7<9?si,sigo;1<9?si,sigo;10<9?no,paro     12>9?si,retrocedo1;13>9?si,ret1;5>9?no,paro
6) [9, 3, 5, 7, 1, 5i, 10d, 13, 12, 16]intercambio
7) [9, 3, 5, 7, 1, 5d, 10i, 13, 12, 16]5<9?si,sigo;10<9?no,paro;                10>9?si,ret1
8) [9, 3, 5, 7, 1, 5d, 10i, 13, 12, 16] d<i 
   [5, 3, 5, 7, 1, 9d, 10i, 13, 12, 16] intercambio d con pivote
     
segunda pasada(0,4)
pivot = 5

   [5, 3, 5, 7i, 1d, 9, 10, 13, 12, 16]3<5?si,sigo;5<=5?si,sigo 7<5?no,paro      1>5?no,paro
   [5, 3, 5, 1i, 7d, 9, 10, 13, 12, 16] intercambio
   [5, 3, 5, 1d, 7i, 9, 10, 13, 12, 16]1<5?si,sigo 7<5?no,paro            7>5?si,ret1
   [5, 3, 5, 1d, 7i, 9, 10, 13, 12, 16] d<i
   [1, 3, 5, 5d, 7i, 9, 10, 13, 12, 16]intercambio
   
tercera pasada (0,2)
pivot = 1














