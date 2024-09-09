x, y = [float(n) for n in input("input (x, y): ").split()]

belongs_1 = x > 0 and y > 0

print(f"Те, що точка ({x}, {y}) належить до 1ї координатної четверті є {belongs_1}")