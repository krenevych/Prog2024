x = float(input("x = "))

if x < -1:
    print(-x**2 + 1)
elif abs(x) <= 1:
    print(0)
else:
    print(x**2 - 1)
