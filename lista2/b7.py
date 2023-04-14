n1, n2, n3, n4, n5, n6 = map(int, input().split())

sum = n1+n2+n3+n4+n5+n6

if sum >= 250:
    print("S+")
elif sum >= 200:
    print("S")
elif sum >= 180:
    print("S-")
elif sum >= 150:
    print("A+")
elif sum >= 100:
    print("A")
elif sum >= 80:
    print("A-")
elif sum >= 60:
    print("B+")
elif sum >= 40:
    print("B")
else:
    print("B-")