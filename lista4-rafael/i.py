n = int(input())
lista = [int(x) for x in input().split()]
valorFinal = 0
i = 0 
cont = 0
while(i<n-1):
    if(lista[i] == 0):
        break
    if(cont >= n):
        break
    valorFinal += lista[i]
    i+=lista[i]
    cont+=1
    

if(valorFinal == n-1):
    print("true")
else:
    print("false")