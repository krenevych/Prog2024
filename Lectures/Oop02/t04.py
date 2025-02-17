class NewClass:
    def __init__(self, name, lastname):
        self.name = name

    def __del__(self):
        # код, що викликається на знищенні обʼєкту
        print(f"Обʼєкт {self.name} знищено")

a1 = NewClass("NewClass 01", "LastName 01")
# a1.__init__("NewClass 01", "LastName 01")
a2 = NewClass("NewClass 02", "LastName 02")
del a1

print("Програма завершується...")
