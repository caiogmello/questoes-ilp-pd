matriz = []

for i in range(8):
  lista = [int(x) for x in input().split()]
  matriz.append(lista)

x, y = map(int, input().split())
count = 0

for i in range((x-1),-1,-1):
  if matriz[x][i] == 1:
    break
  elif matriz[x][i] == 2:
    count+=1
    break

for i in range((x+1),8):
  if matriz[x][i] == 1:
    break
  elif matriz[x][i] == 2:
    count+=1
    break

for i in range((y-1),-1,-1):
  if matriz[i][y] == 1:
    break
  elif matriz[i][y] == 2:
    count+=1
    break


for i in range((y+1),8):
  if matriz[i][y] == 1:
    break
  elif matriz[i][y] == 2:
    count+=1
    break

print(count)
