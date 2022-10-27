def sort(first, second):
    if first < second:
        return (first, second)
    else:
        return (second, first)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a, b = sort(a, b)
b, c = sort(b, c)
a, b = sort(a, b)

if a <= d and b <= e:
    print("YES")
else:
    print("NO")