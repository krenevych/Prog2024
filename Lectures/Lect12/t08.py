# f = open("fibonaci.txt")
#
#
# f.close()

suma = 0
with open("fibonaci.txt") as f:  # після виходу з цього блоку with файл автоматично закривається
    for line in f:
        a = int(line)
        suma += a

print(f"сума елементів файлу = {suma}")