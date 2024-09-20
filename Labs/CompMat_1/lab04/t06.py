n = 1207

inv = 0
while n > 0:
    d = n % 10
    inv = inv * 10 + d
    n = n // 10

print(inv)