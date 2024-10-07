# підпрограма, що визначає чи є задане число N простим
def is_prime(N):  # N - число яке ми будемо перевіряти чи воно просте
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:  # якщо поділилося без остачі,
            return False  # то число не просте
    return True


########### Головна програма ###########
lst = [int(el) for el in input().split()]

# Визначити ті з чисел, які є простими

for n in lst:
    # код перевірки чи число n є простим
    if is_prime(n):
        print(n)

#
p13 = is_prime(13)
print(p13)
p12 = is_prime(12)
print(p12)





















