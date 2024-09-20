n =  int(input())

# Знайти значення факторіалу цілого числа n.
# 1 * 1 * 2 * 3 * 4 * 5
# 0   1   2   3

fact = 1
i    = 0

while i < n:
    i = i + 1
    fact = fact * i

print(fact)