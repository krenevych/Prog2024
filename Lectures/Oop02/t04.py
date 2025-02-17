class NewClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        # код, що викликається на знищенні обʼєкту
        print(f"Обʼєкт {self.name} знищено")

a1 = NewClass("NewClass 01")
a2 = NewClass("NewClass 02")

print("Програма завершується...")
