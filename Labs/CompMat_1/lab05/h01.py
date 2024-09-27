
n = int(input())

suma_even = 0
contains_even = False

while n > 0:
    d = n % 10
    if d % 2 == 0:
        contains_even = True
        suma_even += d

    n = n // 10

if contains_even:
    print(suma_even)
else:
    print(-1)