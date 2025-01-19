a = "Изучаем язык Питон "
words = a.split()
print(words)
dic = {}
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
for word, col in dic.items():
    print(f"{word}: {col}")