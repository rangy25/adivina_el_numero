# programa para adivinar un numero al azar entre 1 y 10
from random import*

#input
X = int(input("ingresar un numero entre 1,10 : "))

#processing and output
Y = randint (1,10)

if X == Y:
    print( " has adivinado el numero ",Y,)
elif X>Y:
    print( " el numero ingresado",X,"es mayor al numero al adivinar",Y,)
else:
    print( " el numero ingresado",X,"es menor que el numero al adivinar",Y,)