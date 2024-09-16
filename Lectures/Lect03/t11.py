N = int(input("N = ?"))

champion = float(input(f"a[{1}] = ?"))
for i in range(N-1): # до N-1, бо перше число ми вже зчитали раніше
    a = float(input(f"a[{i+2}] = ?"))
    if champion < a:
        champion = a

print(f"Найбільше серед заданих числе буде {champion}")

