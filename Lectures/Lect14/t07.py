# 1 / 0

n = int(input("Задайте число "))


try:
    if n == 0:
        raise ZeroDivisionError("Задане вами число є нулем, а ми будемо ділити на нього, а на нуль ділити погана прикмета")
    else:
        print(1/n)
except ZeroDivisionError as e:
    print(e)

# try:
#     raise ZeroDivisionError("division by zero")

