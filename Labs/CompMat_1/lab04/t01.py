n, m = [int(el) for el in input().split()]

# m * n

multiplication = 0
i = 0

while i < m:
# while multiplication != m * n:
    multiplication = multiplication + n
    i = i + 1

print(multiplication)