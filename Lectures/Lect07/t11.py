# Кількість входжень символа у рядок

c = input("c = ")
s = input("s = ")

counter = 0
for a in s:
    if a == c:
        counter += 1

print(counter)