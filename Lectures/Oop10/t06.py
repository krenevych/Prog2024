import math

x = 2
eps = 0.0000001 # точність

S = 1
a = 1
n = 0

while abs(a) >= eps:
    n += 1
    a *= x / n
    S += a

print(f"{S          =}, {n=}")
print(f"{math.exp(x)=}")