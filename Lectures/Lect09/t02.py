def increment_list(a : list):
    a.append(1)
    print(f"{a=}")


########## main #########
A = [1]
print(f"{A=}")
increment_list(A)
print(f"{A=}")
