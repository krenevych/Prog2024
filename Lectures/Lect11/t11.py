# визначити кількість входжень кожного слова до рядка

# hello  world   world    world  hello    world   hello hello

s = "hello  world   world    world  hello  bil gates  world   hello hello"  # тут треба зробити введеня з клавіатури

words = s.split()
print(words)

set_words = set(words)
print(set_words)

words_freq = {}  # словник, що містить пари слово та кількість його входжень
for word in set_words:
    words_freq[word] = words.count(word)

print(words_freq)



