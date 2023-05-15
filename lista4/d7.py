n = int(input())
lista = [int(x) for x in input().split()]

for i in range(n):
    for j in range(i+1, n):
        if lista[j] < lista[i]:
            lista[i], lista[j] = lista[j], lista[i]
        
for i in range(n):
    print(lista[i], end=" ")