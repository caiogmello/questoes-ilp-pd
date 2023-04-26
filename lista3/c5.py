e, p = map(int, input().split())
total = 0
while(e>0):
    if p == 0:
        total = "F"
        break
    e = e-p
    p = p-1
    total = total+1
print(total)