#Recursión numérica

#Función factorial

factorial :: Integer -> Integer
factorial 0 = 1   #caso base
factorial n = n * factorial (n-1) #a
factorial (5)


5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 * factorial(0)
5 * 4 * 3 * 2 * 1 * 1
120

-------------------------------

#Recursión sobre listas

Producto de una lista de números:
product :: Num a => [a] -> a
product []     = 1
product (n:ns) = n * product ns
product [5,2,6,8,3]

product [5,2,6,8,3]
= 5 * product [2,6,8,3]
= 5 * 2 * product [6,8,3]
= 5 * 2 * 6 * product [8,3]
= 5 * 2 * 6 * 8 * product [3]
= 5 * 2 * 6 * 8 * 3 * product []
= 5 * 2 * 6 * 8 * 3 * 1
=1440

--------------------------------------------

#Longitud de una lista:

length :: [a] -> Int
length []     = 0
length (_:xs) = 1 + length xs
lenght [5,2,6,8,3]

1 + length [2,6,8,3]
1 + 1 + length [6,8,3]
1 + 1 + 1 + length [8,3]
1 + 1 + 1 + 1 + length [3]
1 + 1 + 1 + 1 + 1 + length []
1 + 1 + 1 + 1 + 1 + 0
5

--------------------------------

#Inversa de una lista:

reverse :: [a] -> [a]
reverse []     = []
reverse (x:xs) = reverse xs ++ [x]
reverse [5,2,6,8,3]

reverse [2,6,8,3] ++ [5]
reverse [6,8,3] ++ [2] ++ [5]
reverse [8,3] ++ [6] ++ [2] ++ [5]
reverse [3] ++ [8] ++ [6] ++ [2] ++ [5]
reverse [] ++ [3] ++ [8] ++ [6] ++ [2] ++ [5]
[] ++ [3] ++ [8] ++ [6] ++ [2] ++ [5]
[3,8,6,2,5] 

-----------------------------------------------

#Recursión sobre varios argumentos: La función drop

#Eliminación de elementos iniciales:
drop :: Int -> [a] -> [a]
drop 0 xs     = xs
drop n []     = []
drop n (x:xs) = drop (n-1)  xs

drop 3[5,2,6,8,3]


drop (3-1)  [2,6,8,3]
drop 2 [2,6,8,3]
drop (2-1)[6,8,3]
drop 1[6,8,3]
drop 1-1[8,3]
drop 0 [8,3]
[8,3]





--------------------------------------------

#4 Recursión múltiple
#Fibonacci

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-2) + fibonacci (n-1)
fibonacci 8

fibonacci (8-2) + fibonacci (8-1) 
fibonacci 6     +  fibonacci 7
fibonacci 6-2   +  fibonacci 6-1 + fibonacci 7-2 + fibonacci 7-1
fibonacci 4     +  fibonacci 5   + fibonacci 5   + fibonacci 6
fibonacci (4-2) + fibonacci(4-1) + fibonacci(5-2)+ fibonacci(5-1) + fibonacci(5-2) + fibonacci(5-1) + fibonacci(6-2) + fibonacci(6-1)
fibonacci (2)   + fibonacci (3)  + fibonacci(3)  + fibonacci (4)  + fibonacci (3)  + fibonacci (4)  + fibonacci (4)  + fibonacci (5)
fibonacci (2-2) + fibonacci(2-1) + fibonacci(3-2)+ fibonacci(3-1) + fibonacci(3-2) + fibonacci(3-1) + fibonacci(4-2) + fibonacci(4-1) + fibonacci (3-2) + fibonacci (3-1) + fibonacci (4-2) + fibonacci (4-1)+fibonacci (4-2) + fibonacci (4-1)+fibonacci (5-2) + fibonacci (5-1)
fibonacci (0)   + fibonacci (1)  + fibonacci (1) + fibonacci (2)  + fibonacci (1)  + fibonacci (2)  + fibonacci (2)  + fibonacci (3)  + fibonacci (1)   + fibonacci (2)   + fibonacci (2)   + fibonacci (3)  +fibonacci (2)   + fibonacci (3)  +fibonacci (3)   + fibonacci (4)
0               + 1              + 1             + fibonacci(2-2) + fibonacci(2-1) + 1 + fibonacci (2-2) + fibonacci (2-1) + fibonacci (2-2) + fibonacci (2-1)+fibonacci (3-2) + fibonacci (3-1) + 1 + fibonacci (2-2) + fibonacci (2-1) + fibonacci (2-2) + fibonacci (2-1)+fibonacci (3-2) + fibonacci (3-1)+fibonacci (2-2) + fibonacci (2-1)+fibonacci (3-2) + fibonacci (3-1)+fibonacci (3-2) + fibonacci (3-1)+fibonacci (4-2) + fibonacci (4-1)
0               + 1              + 1             +        0       + 1              + 1 + 0               + 1               + 0               + 1              + 1              +  fibonacci (2)  + 1 + 0                + 1               +  0              +  1             + 1              + fibonacci (2)  + 0             + 1              + 1              + fibonacci (2)  + 1              +  fibonacci (2) + fibonacci (2)  + fibonacci (3)
0               + 1              + 1             +        0       + 1              + 1 + 0               + 1               + 0               + 1              + 1              +  fibonacci (2-2) + fibonacci (2-1) + 1 + 0 + 1 + 0 +1 + 1 + fibonacci (2-2) + fibonacci (2-1) + 0 + 1 + 1 + fibonacci (2-2) + fibonacci (2-1) + 1 + fibonacci (2-2) + fibonacci (2-1) + fibonacci (2-2) + fibonacci (2-1) + fibonacci (3-2) + fibonacci (3-1)       
0               + 1              + 1             +        0       + 1              + 1 + 0               + 1               + 0               + 1              + 1              +  0               +  1              + 1 + 0 + 1 + 0 +1 + 1 + 0               +   1             + 0 + 1 + 1 + 0               + 1               + 1 + 0               + 1               + 0               +  1              + fibonacci (1)   + fibonacci (2)
0               + 1              + 1             +        0       + 1              + 1 + 0               + 1               + 0               + 1              + 1              +  0               +  1              + 1 + 0 + 1 + 0 +1 + 1 + 0               +   1             + 0 + 1 + 1 + 0               + 1               + 1 + 0               + 1               + 0               +  1              + 1               + fibonacci (2-2) + fibonacci (2-1)
0               + 1              + 1             +        0       + 1              + 1 + 0               + 1               + 0               + 1              + 1              +  0               +  1              + 1 + 0 + 1 + 0 +1 + 1 + 0               +   1             + 0 + 1 + 1 + 0               + 1               + 1 + 0               + 1               + 0               +  1              + 1               + 0               + 1

=21

---------------------------------------------

#Subir la escalera

formas n::  Int->Int
formas 1 = 1
formas 2 = 2
formas n = formas(n-1) + formas(n-2)
formas 5


formas(4) + formas(3)
formas(3) + formas(2) + formas(2) + formas(1)
formas(2) + formas(1) + 2         + 2        + 1
2         +   1       + 2         + 2        + 1

=8

-----------------------------------------------

#5 Recursión mutua
#Par e impar por recursión mutua:

par :: Int -> Bool
par 0 = True
par n = impar (n-1)

impar :: Int -> Bool
impar 0 = False
impar n = par (n-1)

par (7)

impar (6)
par (5)
impar (4)
par (3)
impar (2)
par (1)
impar (0)
False

----------------------------------

#6 Defina en python todas las funciones anteriores














