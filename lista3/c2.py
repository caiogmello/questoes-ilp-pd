n = int(input())

trad = gel = 0

for i in range(n):
  x = int(input())
  if x == 11:
    gel+=1
  elif x == 10:
    trad+=1


if(gel < trad):
  print("Tradicional")
else:
  print("Geleia")