# Перетворити маленьку
# латинську літеру у відповідну велику

dist = ord("a") - ord("A")
print(dist)

small = "t"

big = chr(ord(small) - dist)

# big = chr(ord("a") - (ord("a") - ord("A")))

print(big)
