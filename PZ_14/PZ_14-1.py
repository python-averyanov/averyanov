# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».
import re
with open('writer.txt', 'r', encoding='utf-8') as f:
    text = f.read()
su = re.findall(r'^[А-ЯЁ][а-яё][а-яё]', text, re.MULTILINE)


u = set(su)
# print(su)
# print(u)
print(f'фамилий: {len(su)}')
print(f'Уникальных фамилий: {len(u)}')

new_text = re.sub(r'\bроман\b', 'произведение', text)

with open('writer_modified.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)
