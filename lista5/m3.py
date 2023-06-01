n = int(input())
matriz = []

for i in range(n):
  lista = [int(x) for x in input().split()]
  matriz.append(lista)

harry = 0
ron = 0

x,y = map(int, input().split())

for i in range(n):
  ron += matriz[i][y]
  matriz[i][y] = 0
  harry += matriz[x][i]
  matriz[x][i] = 0


print(f'Harry {harry}')
print(f'Ron {ron}')
      

