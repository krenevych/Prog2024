# написати рекурсивну функцію перевірки рядка на симетричність

# asdsa
# asdTa

# "a"  "" - тривіальний випадок - порожній рядок або рядок з одного елементу є симетричним
# "aasdsdsaa"
# "asdsdsa"
# "sdsds"
#

def is_symetric(s):
    if len(s) <= 1: # порожній рядок або рядок з одного елементу є симетричним
        return True
    else:
        return s[0] == s[-1] and is_symetric(s[1:-1])

print(is_symetric('dcacd'))
print(is_symetric('dAbcd'))
print(is_symetric('dAbcD'))