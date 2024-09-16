# Знайти суму парних чисел з діапазону від 1 до N

suma = 0

N = int(input("N = "))
for i in range(2, N + 1, 2):
    suma += i
    # print(i)

print(f"Sum = {suma}")

print("using sum: ", sum(range(2, N + 1, 2)))