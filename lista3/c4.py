t = int(input())
retorno = "O Havai pode dormir tranquilo"

while(True):
  p = int(input())
  if p==0:
    break
  if(p>t):
    retorno = "ALARME"

print(retorno)