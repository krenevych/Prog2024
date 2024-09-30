# print("A" < "7")

# Вивести на екран всі великі літери латинського алфавіту

for code in range(ord("A"), ord("Z") + 1):
    char = chr(code)
    print(char, end=" ")