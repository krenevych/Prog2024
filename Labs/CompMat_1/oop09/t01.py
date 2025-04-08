import math

xk = 1
x = float(input("x= "))
n = int(input("n= "))
for k in range(1, n+1):
    # xk = -xk * x**2 / ((2*k -1) * 2 * k)
    print(x ** (2*k), math.factorial(2 * k))
    xk = (-1) ** k * x ** (2*k) / math.factorial(2 * k)
    print(xk)