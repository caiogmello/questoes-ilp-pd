matriz = []

for i in range(10):
    lista = [input().split()]
    matriz.append(lista)

mago_aliado = False
mago_inimigo = False

O = 0
H = 0

for i in range(10):
    for j in range(5):
        if matriz[i][j] == "m":
            mago_inimigo = True

for i in range(10):
    for j in range(5,10):
        if matriz[i][j] == "m":
            mago_inimigo = True

for i in range(10):
    for j in range(10):
        if matriz[i][j] == "o":
            tempPower = 1