u = 0
v = 1
w = 1

for i in range(2, 7):
    u, v, w = v, w, u + v + w

print(f"{u=}, {v=}, {w=}")