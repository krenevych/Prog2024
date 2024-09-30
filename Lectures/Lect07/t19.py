s = "    Hello,     World!    I'm   \t  Andrii\nI'm      teacher  of    programming and   math"

# s = input()

print(s)
words = s.split()
print(f"кількість слів у заданому рядку буде {len(words)}")
print(words)
s = " ".join(words)
print(s)