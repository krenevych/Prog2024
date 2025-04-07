
N = 10

x = 0.7
an = 1  # an - змінна, що зберігає поточний член послідовності

for n in range(1, N+1):
    an = x / n * an

print(an)