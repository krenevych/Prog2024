a, b, c = [float(el) for el in input().split()]

assert (a > 0 and b > 0 and c > 0
        and a + b > c
        and a + c > b
        and c + b > a), "Трикутник з такими сторонами не існує"

p = a + b + c
p = p / 2

# Формула Герона
s = p * (p - a) * (p - b) * (p - c)
s = s ** 0.5

print(f"Площа трикутника зі сторонами {a}, {b}, {c} = {s}")


