n = int(input())

t = 0

for i in range(n):
    nome, k = input().split()
    k = int(k)
    t += k

c = int(input())

if t <= c:
    print("Vamos todos encontrar a montanha!")
else:
    print("Vamos virar almoço de aranhas gigantes!")
