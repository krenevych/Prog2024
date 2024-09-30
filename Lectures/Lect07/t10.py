# Переревірити чи є рядок симетричним
# abcba - симетричний, abcaa - не симетричний

origin = input()

# 1. порівнювати рівновіддалені від середини (від початку і кінця) символи

is_sym = True
for i in range(len(origin) // 2):
    if origin[i] != origin[-i-1]:
        is_sym = False
        break

print(is_sym)


# 2. зробити інверсію рядка і порівняти з вихідним
print(origin == origin[::-1])
