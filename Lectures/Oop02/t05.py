class NewClass:
    def __init__(self, name):
        self.name = name
        print(f"Обʼєкт {self.name} створено")

    def __del__(self):
        print(f"Обʼєкт {self.name} знищено")

a1 = NewClass("Object 01")
a1_copy_ref = a1
del a1  # деструктор не буде викликаний, бо є ще одне посилання на обʼєт Object 01
del a1_copy_ref

print("Програма завершується...")
