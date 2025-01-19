file = open('writer.txt', 'r', encoding='utf-8')

for i in file:
    if i.split():
        first = i.split()[0]
    else:
        ''
    print(first)


