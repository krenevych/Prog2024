N = 10
f2 = 1
f1 = 1
i = 1

while i < N:
# for i in range(2, N+1):
    i += 1
    f2, f1 = f1, f2 + f1

print(f"{f2=}, {f1=}")
