# (E1_T01_P_01)  Знайдіть скільки простих чисел міститься у проміжку (1_000, 10_000).
#  Відомо, що в проміжку (500, 1000) міститься 73 простих числа

# 7 - просте число, бо воно ділиться лише на 1 і на 7

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # число не просте!!!
    return True

############ main ##########

counter = 0
for i in range(500, 1001):
    if is_prime(i):
        counter = counter + 1

print(counter)