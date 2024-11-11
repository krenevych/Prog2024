try:
    with open("input.txt") as f:
        print(1 / int(f.read()))       # Обробка файлу
except FileNotFoundError:
    print("Такий файл не існує")
