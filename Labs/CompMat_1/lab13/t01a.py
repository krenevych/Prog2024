# f = open("input01.txt", "rt")
# # працюємо з файлом
# f.close()

with open("input01.txt", "rt") as f:
    for line in f:
        print(line, end="")