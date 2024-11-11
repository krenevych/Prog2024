with open("output.txt", "w") as f:
# f = open("output.txt", "w")
    print(12, file=f)
    print(144, file=f)
    print(1 / 0, file=f)  # Обробка файлу
# f.close()
