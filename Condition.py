troom, tcond = map(int, input().split())
level = input().lower()

if level == "heat":
    if troom > tcond:
        print(troom)
    else:
        print(tcond)
elif level == "freeze":
    if troom > tcond:
        print(tcond)
    else:
        print(troom)
elif level == "fan":
    print(troom)
elif level == "auto":
    print(tcond)
else:
    print("")