

def part(n, current):
    if n == 0:
        print(*current)
    else:
        for i in range(1, n + 1):
            new_current = current.copy()
            new_current.append(i)
            part(n - i, new_current)


###### main ########

part(4, [])