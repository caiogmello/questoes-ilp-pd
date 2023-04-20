n, q = map(int, input().split())
soma = 0
for i in range(n):
  soma += q
  q=q*2
print(soma)