n = int(input())
amigos = [int(x) for x in input().split()]

t = int(input())

for i in range(t):
    q = int(input())
    turma = [int(x) for x in input().split()]
    count = 0
    for j in range(n):
        if amigos[j] in turma:
            count += 1
    if(count == n):
        print("Todos reunidos!")
    else:
        print(count)

