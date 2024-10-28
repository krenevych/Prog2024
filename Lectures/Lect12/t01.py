# f = open("input.txt")  # 1. Відкриття файлу
f = open("input.txt", "rt")  # 1. Відкриття файлу

list_of_lines = []
for line in f:  # 2. Робота з файлом
    # print(line)
    print(line, end="")
    # list_of_lines.append(line)

f.close()  # 3. Закриття файлу
