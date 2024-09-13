
# число n непарне;
# • число n додатне і трицифрове.

n = int(input())

cond_odd = n % 2 != 0
cond_positive_3 = 99 < n < 1000

if cond_odd or cond_positive_3:
    print("YES")
else:
    print("NO")



