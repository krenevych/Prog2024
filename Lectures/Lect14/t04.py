lst = [1, 2, 3]
d = {1: "1", 2 : "два", 4: "four"}

collection = lst
# collection = d

try:
    print(collection[22])
except LookupError as e:
    print(f"Такого елемента не існує {type(e)}")

# except IndexError as e:
#     print(f"Такого елемента не існує {type(e)}")
# except KeyError as e:
#     print(f"Такого елемента не існує {type(e)}")