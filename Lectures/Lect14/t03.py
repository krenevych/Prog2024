# У файлі міститься ціле число n,
# треба обчислити обернене до нього 1/n

f = None
try:
    f = open("input.txt")
    int_from_file = int(f.read())
    inv = 1 / int_from_file
    print(inv)
    # f.close()
    lst = [1, 2, 3]
    print(lst[100])
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Число, що міститься у файлі є нулем")
except IndexError as err:  # err - екземпляр виключення, що містить інформацію, про помилку, що виникла
    print(f"Відбулася спроба взяти не існуючий елемент зі списку: {err}")
# except:  # блок, що перехоплює всі виключення - категорично не рекомендується використовувати його у програмі
#     print("Жоден з типів виключень не підійшов")
else:  # відпрацює, якщо блок try виконався без помилки-виключення
    print("Else")
finally:  # виконується у будь-якому разі, не залежно від того, чи виникла у блоці try-except помилка
    print("Finally")
    if f is not None:
        f.close()

print("finish")

# Else
# Finally

# Finally
