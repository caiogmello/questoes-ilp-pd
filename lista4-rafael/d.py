n = int(input())
lista = [int(x) for x in input().split()]

totalSum = 0
actualSum = 0

for i in range(n):
    totalSum+=lista[i]

for i in range(n):
    actualSum+=lista[i]
    if actualSum == totalSum/2:
        print(i + 1)
        break

