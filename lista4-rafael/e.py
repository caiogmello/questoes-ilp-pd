# errada

n, p = map(int, input().split())

listaPresentes = [int(x) for x in input().split()]
listaTotal = [int(x) for x in range(1, n+1)]

listaPresentes.sort()
listaTotal.sort()

for i in range(p):
    listaTotal.remove(listaPresentes[i])

for i in range(len(listaTotal)):
    print(listaTotal[i], end=' ')
