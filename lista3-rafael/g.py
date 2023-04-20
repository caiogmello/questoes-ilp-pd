n = int(input())
ini = 1

for i in range(n):
  print(" "*(n-i-1) + str(i+1)*ini)
  ini+=2

    