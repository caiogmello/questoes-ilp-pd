n = int(input())
lista = [int(x) for x in input().split()]
c = int(input())

saida = -1

for i in range(n):
    if lista[i] == c:
        saida = c
        break

print(saida)
