n = int(input())
lista = [int(x) for x in input().split()]
forca = int(input())

for i in range(n):
    if lista[i] >= forca/2:
        print(i, end=" ")

