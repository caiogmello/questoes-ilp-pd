n = int(input())
value = -1
lista = [int(x) for x in input().split()]

for i in range(1, n):
    if lista[i] == lista[i-1]:
        value = lista[i]
        break
print(value)