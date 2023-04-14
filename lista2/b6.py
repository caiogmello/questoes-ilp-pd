a, m, c = map(int, input().split())

maximo = 0

if a>=2 and m>=3 and c>=5:
    maximo = a//2
    if (m//3) < maximo:
        maximo = m//3
    if (c//5) < maximo:
        maximo = c//5
        
print(maximo)