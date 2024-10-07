# Визначити цифру, що входить до запису
# натурального числа
# найбільшу кількість разів та кількість її входжень.

def frequency(n):
    # Побудова списку кількості входжень кожної цифри
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   - список частот
    #  0  1  2  3  4  5  6  7  8  9    - індекси, вони ж відповідають цифрам числа
    freq = [0] * 10
    while n > 0:
        d = n % 10
        freq[d] += 1
        n = n // 10
    return freq

def most_popular_digit(N):
    freq_lst = frequency(N)
    maxD = -1
    maxCount = 0
    for d, curCount in enumerate(freq_lst):
        if curCount > maxCount:
            maxD, maxCount = d, curCount

    return maxD, maxCount  # повертає цифру та кількість її входжень

########## Головна програма після опису всіх функцій ##########
# n = 1234332
# freq_lst = frequency(n)
# print(freq_lst)

n = 1234332
d, count = most_popular_digit(n)
print(d, count)