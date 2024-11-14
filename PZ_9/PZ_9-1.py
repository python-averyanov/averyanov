a = "Изучаем язык Питон "
words = a.split()
dic = {}
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
for word, co in dic.items():
    print(f"{word}: {co}")