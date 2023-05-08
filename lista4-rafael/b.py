#  errada

n = int(input())
lista = [int(x) for x in input().split()]

for i in range(n, 0,-1):
    print(f"{i}: {lista[i-1]}")