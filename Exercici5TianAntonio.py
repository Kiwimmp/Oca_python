# Antonio Tian 1DAM presncial
import random
casilla = int(input("Dime cuantas casillas hay: "))
posicion = 0
tirada = 0
print(f"Estoy en la posición {posicion}")
while posicion != casilla:
    tirada += 1
    dado = random.randint(1, 6)
    posicion = posicion + dado
    print(
        f"He sacado un {dado} , avanzo a la posición {posicion}. Número de tirada {tirada}")
    if posicion == casilla:
        break
    if posicion > casilla:
        rebote = posicion - casilla
        posicion = posicion - rebote*2
        print(f"He rebotado {rebote} y he vuelto a la posición {posicion} ")
        continue
    if posicion % 5 == 0:
        posicion += 5
        print(
            f"De oca a oca y tiro porque me toca. Estoy en la posición {posicion}")
print(f"He ganado con {tirada} tiradas")
