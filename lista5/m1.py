n, m = map(int, input().split())
matriz = []

for i in range(n):
  lista = [int(x) for x in input().split()]
  matriz.append(lista)

p = int(input())

cont = 0

for i in range(n):
  for j in range(m):
    if matriz[i][j] == p:
      cont += 1

print(f'Ash pegou {cont} pokemon')