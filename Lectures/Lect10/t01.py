# 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5  6  7  8
def F(n):
    if n == 0 or n == 1: # термінальна гілка рекурсії
        return 1
    else:
        return F(n-1) + F(n-2)  # рекурсивна гілка = виклик себе з іншими аргументами

######## main ################

print(F(41))

# for i in range(10):
#     print(F(i))
