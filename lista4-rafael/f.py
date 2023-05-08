n, m = map(int, input().split())
navios = [int(x) for x in input().split()]
bombas = [int(x) for x in input().split()]

afundados = 0

for i in range(m):
    if(navios[bombas[i]] == 1):
        if(navios[bombas[i]-1] == 1 and navios[bombas[i]+1] == 1):
            afundados += 1

print(afundados)