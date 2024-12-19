# (E1_T01_P_11) Скільки серед простих чисел, що місяться у проміжку (10_000, 20_000) міститься чисел,
# що є паліндромами?.
#
#  Відомо, що проміжок (100, 1000) міститься 15 таких числа.

# Вправа!!!
#  (E1_T01_P_05) Скільки чисел, міститься у проміжку (10_000, 100_000), таких, що їхні
#  квадрати є паліндромами.
#  Відомо, що проміжок (1000, 50000) міститься 11 таких числа.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  # число не просте!!!
    return True


# def is_palindrom(n): - чітерство, бо рядки
#     n1 = str(n)
#     n2 = n1[::-1]
#     return n1 == n2

# 0
# 4321
def is_palindrom(n):
    reversed = 0
    N = n
    while N > 0:
        d = N % 10
        reversed = reversed * 10 + d
        N = N // 10

    return reversed == n

######### main ##############

# print(is_palindrom(1234))     # False
# print(is_palindrom(1234321))  # True

counter = 0
for i in range(10_000, 20_000):
    if is_prime(i) and is_palindrom(i):
        counter += 1

print(counter)
