def func(a):
    b = 10  # локальна змінна функції func
    print(b)


######## main ########

b = "Hello"  # Глобальна змінна
func(100500)
print(b)