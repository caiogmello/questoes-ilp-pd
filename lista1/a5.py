q1, q2, q3 = map(int, input().split())
e1, e2, e3 = map(int, input().split())

sobraram = (q1+q2+q3)-(e1+e2+e3)*3
print(sobraram)