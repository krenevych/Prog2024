def is_square(n):
    n_2 = (n ** 0.5)
    n_2_int = int(n_2)
    n_2_int_square = n_2_int ** 2
    return n_2_int_square == n

def is_pow5(n):
    while n > 1:
        if n % 5 != 0:
            return False
        n = n // 5
    return True

def is_prime(N):  # N - число яке ми будемо перевіряти чи воно просте
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:  # якщо поділилося без остачі,
            return False  # то число не просте
    return True

##### main #########

numbers = [int(el) for el in input().split()]
primes = []
pow5s = []
squares = []
for n in numbers:
    if is_pow5(n):
        pow5s.append(n)
    if is_square(n):
        squares.append(n)
    if is_prime(n):
        primes.append(n)

print("Прості числа  ", primes)
print("Повні квадрати", squares)
print("Степені 5     ", pow5s)