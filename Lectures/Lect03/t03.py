# Знайти суму цифр заданого натурального числа

n = int(input("Задайте натуральне число "))

# 2345 % 10

suma = 0
origin_n = n
while n > 0:
    last = n % 10
    suma += last
    n //= 10 # n = n // 10

print(f"Сума цифр числа {origin_n} = {suma}")