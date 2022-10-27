a = int(input())
b = int(input())
n = int(input())
m = int(input())
min1 = (a + 1) * (n - 1) + 1
max1 = (a + 1) * (n - 1) + 1 + 2 * a
min2 = (b + 1) * (m - 1) + 1
max2 = (b + 1) * (m - 1) + 1 + 2 * b
min_real = max(min1, min2)
max_real = min(max1, max2)
if max_real < min_real:
    print(-1)
else:
    print(min_real, max_real)