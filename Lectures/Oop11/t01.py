
try:
    s = 1/0
    print(s)
except ZeroDivisionError as er:
    print(er)