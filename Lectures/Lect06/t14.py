a = (1, 2, 3, 4, 5, 6)
b = a
a = a[:2] + a[4:]
print(a)
print(b)
