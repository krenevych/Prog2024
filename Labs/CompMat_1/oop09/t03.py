S = 1
a = 1
for n in range(2, 11): # 10-й член послідовності
    a = -a
    S += a  / n

print(S)