M = {1, 2, }  # звичайна множина
N = frozenset((2, 3, 4)) # незмінювана множина
K = frozenset((3, 4, 5)) # незмінювана множина

U = M | N # {1, 2, 3, 4} - звичайна множина, бо першим операндом є звичайна множина
print(U)

U = N | M  # frozenset({1, 2, 3, 4}) - незмінювана множина, бо першим операндом є незмінювана множина
print(U)

# x = M.pop()
# print(x)

# x = N.pop()
# print(x)

N_old = N

N = N | {5}
print("new N=",N)
print(f"{N_old=}")

