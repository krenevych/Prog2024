a, b, c = [int(x) for x in input().split()]

# print(a, b, c)
if (a**2 + b**2 == c**2
        or a**2 + c** 2 == b**2
        or c**2 + a**2 == b**2):
    print("YES")
else:
    print("NO")

pass