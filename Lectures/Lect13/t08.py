

lst = []
try:
    elem = lst.pop()  # може містити потенційну помилку
    print("останній елемент списку є", elem)
except IndexError:
    print("Людино, здається ти не сповна розуму, щоб брати елемент з порожнього списку")

pass