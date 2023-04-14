z, g = input().split()
d, c = input().split()

if(z!=d):
    print("Bloqueado")
else:
    print("Driblado")
    if(g!=c):
        print("...e o goleiro pega")
    else:
        print("Gol")