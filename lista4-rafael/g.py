n = int(input())
lista = [int(x) for x in input().split()]

for i in range(n):
    for j in range(n):
        if lista[j] == i+1:
            print(j+1, end=' ')
