matriz = []

n, m = map(int, input().split())


for i in range(n):
  lista = [int(x) for x in input().split()]
  matriz.append(lista)

count = 0

for i in range(m):
    x, y = map(int, input().split())
    for j in range((x-1), -1, -1):
        if matriz[j][y] == 1:
            matriz[j][y] = 0
            count +=1
            break
    
print(count)
