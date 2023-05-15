s, n = map(int, input().split())

lista = [0]*n
lista[0] = 1

for i in range(s):
    p = int(input())
    temp = p
    while temp < n:
        lista[temp] = 1
        temp += p

for i in range(n-1):
    print(lista[i], end=' ')

print(lista[n-1])
