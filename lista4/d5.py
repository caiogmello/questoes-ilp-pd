n = int(input())
fases = [int(x) for x in input().split()]
m = int(input())

life = m

retorno = "Yes, you can"

for i in range(n):
    if fases[i] == 1:
        life = m
    elif fases[i] >= 2:
        life -= fases[i]
        if life <= 0:
            retorno = "You Died"
            break

print(retorno)