f,c = map(int, input().split())
matriz = []

for i in range(f):
  lista = [int(x) for x in input().split()]
  matriz.append(lista)

assentos = [1,1]
fileira = 1
for i in range(f):
  for j in range(c-1):
    if matriz[i][j] == 0 and matriz[i][j+1] == 0:
      assentos[0] += j
      assentos[1] += j+1
      fileira += i
      break

print(f'Fileira: {fileira}')
print(f'Assentos: {assentos[0]} e {assentos[1]}')
      

