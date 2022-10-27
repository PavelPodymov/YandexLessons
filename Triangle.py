x = int(input())
y = int(input())
z = int(input())

if (x + y) > z and (z + y) > x and (x + z) > y:
    print("YES")
else:
    print("NO")