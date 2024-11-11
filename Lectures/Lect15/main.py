import my_module

res2 = my_module.my_pow2(2)
res3 = my_module.my_pow3(2)

print(res3, res2)

print("Імʼя головного модуля = ", __name__)
print("Імʼя імпортованого модуля = ", my_module.__name__)