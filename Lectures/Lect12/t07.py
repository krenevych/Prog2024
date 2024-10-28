fib_file = open("fibonaci.txt", "w")


F1 = 1
# fib_file.write(str(F1) + "\n")
F2 = 1
# fib_file.write(str(F2)+ "\n")
print(F2, file=fib_file)
print(F1, file=fib_file)
for i in range(2,100):
    F2, F1 = F1, F2 + F1
    print(F1, file=fib_file)
    # fib_file.write(str(F1)+ "\n")

fib_file.close()