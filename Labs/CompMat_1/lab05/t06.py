n = int(input())

is_prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(1)
else:
    print(0)
