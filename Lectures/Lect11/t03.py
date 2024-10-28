
s = input()

# порахувати скільки в введеному з клавіатури рядку є різних симовлів
# та скільки разів кожен символ входить в цей рядок

frequency = {ch : s.count(ch) for ch in s}

# abbbba444d44
print(f"{frequency=}")
print("кількість різних символів у введеному рядку = ", len(frequency))

# порахувати скільки в введеному з клавіатури рядку є різних цифр
# та скільки разів кожна цифра входить в цей рядок


frequency = {ch : s.count(ch) for ch in s if ch.isdigit()} # ch.isdigit() - чи є ch цифрою

# abbbba444d44
print(f"{frequency=}")
print("кількість різних цифр у введеному рядку = ", len(frequency))

# чи є в рядку цифра, що зустрічається 5
if 5 in frequency.values():
    print("Зустрічається")
else:
    print("Не зустрічається")









