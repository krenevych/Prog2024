def is_prime(N):  # N - число яке ми будемо перевіряти чи воно просте
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:  # якщо поділилося без остачі,
            return False  # то число не просте
    return True


################ main program ################

n = int(input("Enter a number: "))

for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
