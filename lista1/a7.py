segundos = int(input())

restoSegundos = segundos%3600
horas = segundos//3600
minutos = restoSegundos//60
segundos = restoSegundos%60

print(f"{horas}h {minutos}m {segundos}s")