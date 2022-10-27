a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif a == 0 and b == c**2 and c >= 0:
    print("MANY SOLUTIONS")
else:
    if a != 0:
        x = (c ** 2 - b) / a
        if x == round(x, 0):
            print(int(x))
        else:
            print("NO SOLUTION")
    else:
        print("NO SOLUTION")