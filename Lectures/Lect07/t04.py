# Послідовність Фібоначчі

#             u
#                 v
#                u+v
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# 0  1  2  3  4  5   6   7

u = 1
v = 1

for i in range(2, 6):
    u, v = v, u + v
    print(v)

# for i in range(2, 6):
#     n = u + v
#     u = v
#     v = n

print(v)

