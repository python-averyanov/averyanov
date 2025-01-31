a = "Изучаем язык Питон Питон "
words = a.split()
print(words)
dic = {}
for i in words:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i, col in dic.items():
    print(f"{i}: {col}")