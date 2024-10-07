lst = [int(el) for el in input().split()]

# Визначити ті з чисел, які є простими

for n in lst:
    # код перевірки чи число n є простим
    is_prime = True  # спочатку вважаємо, що число є простим
    for i in range (2, n-1):
        if n % i == 0:  # якщо поділилося без остачі,
            is_prime = False  # то число не просте
    if is_prime:
        print(n)

# print(lst)