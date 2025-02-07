#Используя словарь посчитать количество уникальных слов в заданном
#предложении «Изучаем язык Питон». Вывести на экран каждую пару
#«ключ:значение»

a = "Изучаем язык Питон Питон JS"
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