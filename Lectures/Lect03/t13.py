# задано послідовність чисел, що завершується 0.
# Знайти найбільше серед додатних

max_positive = 0
while True:
    a = int(input("Задайте ціле число (0 для завершення) "))
    if a == 0:
        break

    if a < 0: # якщо ми ввели від'ємне число, що переходимо на початок цикло для введення наступного числа
        continue

    if max_positive < a:
        max_positive = a

print(f"{max_positive = }")   # print(f"max_positive = {max_positive}")