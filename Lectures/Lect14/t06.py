while True:
    a, b, c = [float(el) for el in input("a, b, c? ").split()]
    try:
        assert a > 0 and b > 0 and c > 0, \
            "Всі сторони трикутника мають бути додатніми"

        assert a + b > c and a + c > b and c + b > a, \
            "Трикутник з такими сторонами не існує (не виконується нерівність трикутника)"
    except AssertionError as err:
        print(err, "спробуйте ще раз задати сторони трикутника")
        continue
    break

p = a + b + c
p = p / 2

# Формула Герона
s = p * (p - a) * (p - b) * (p - c)
s = s ** 0.5

print(f"Площа трикутника зі сторонами {a}, {b}, {c} = {s}")
