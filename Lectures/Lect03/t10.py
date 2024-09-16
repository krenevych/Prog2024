N = int(input("N = ?"))

champion = -100500  # crutch,
for i in range(N):
    a = float(input(f"a[{i+1}] = ?"))
    if champion < a:
        champion = a

print(f"Найбільше серед заданих числе буде {champion}")

