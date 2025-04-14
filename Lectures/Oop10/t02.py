f2 = 1
f1 = 1

for i in range(2, 11):
    f2, f1 = f1, f2 + f1

print(f"{f2=}, {f1=}")