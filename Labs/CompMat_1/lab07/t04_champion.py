# Дано деяке речення на невідомій мові.
# Назвемо слово у ньому чемпіоном, якщо воно
# є паліндромом і кількість літер у ньому максимальна.
# Літерами алфавіту у невідомій мові є літери латинського алфавіту
# та арабські цифри.
# Гарантується, що у реченні відсутні # інші символи, крім літер,
# пропусків, розділових знаків та нелітерних дефіс (мінус) і апостроф.
import string

# Oo ,,,, tt aaa-aaa is not bb.
# Oo - tt aaa-aaa is not bb

sentence = input().lower()

# if "'" in sentence:
#     raise RuntimeError()
#     # print(0 / 0)

sentence = sentence.replace(" - ", " ")

sentence_clean = ""
for letter in sentence:
    if letter.isalpha():
        sentence_clean += letter
    elif letter == "-":
        sentence_clean += "-"
    else:
        sentence_clean += " "

# print(sentence_clean)

sentence = sentence_clean

champion = ""
champion_len = 0
champion_pos = -1
words = sentence.split()
for i, word in enumerate(words):
    if word == word[::-1]:
        if champion_len < len(word):
            champion = word
            champion_len = len(word)
            champion_pos = i + 1


# print(champion)
# print(champion_len)
# print(words.index(champion) + 1)
print(champion_pos)
