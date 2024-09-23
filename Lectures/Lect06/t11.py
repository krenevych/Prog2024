N = int(input("Задайте кількість елементів у списку "))

lst = []
for i in range(N):
    a = int(input(f"a[{i}] = "))
    lst.append(a)

print(lst)