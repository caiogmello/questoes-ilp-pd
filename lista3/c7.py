n = int(input())
lvl = 1
for i in range(n):
  c, p = input().split()
  p = int(p)
  if c == "t":
    lvl += p
  elif c == "m":
    print("Combate iniciado")
    if(lvl>=p):
      print("VITORIA")
      lvl += 1
    else:
      print("Derrota! Fim da aventura")
      break
  elif c == "b":
    lvl -= p
    if lvl < 0:
      lvl = 0
  if lvl >= 5:
    print("Aventura concluida")
    break
print()
    
    