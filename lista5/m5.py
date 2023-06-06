matriz = []

n, m = map(int, input().split())

for i in range(n):
  lista = [int(x) for x in input().split()]
  matriz.append(lista)

out1 = 0
out2 = 0

for i in range(n):
    for j in range(m):
        if matriz[i][j] != 0:
            continue
        else:
            if matriz[i+1][j] != 1 or matriz[i][j+1] != 1 or matriz[i-1][j] != 1 or matriz[i][j-1] != 1:
                break
            else:
                out1 = i
                out2 = j
                break

print(out1, out2)

