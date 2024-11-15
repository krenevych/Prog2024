s = "boing 777"


suma = 0
for c in s:
    try:
        suma += int(c)
    except ValueError:
        continue

print(suma)