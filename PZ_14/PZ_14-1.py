# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
# фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
# «произведение».
import re
with open('writer.txt', 'r', encoding='utf-8') as f:
    text = f.read()
surnames = re.findall(r'\b[А-ЯЁ][а-яё]+\b', text)

unique= set(surnames)
print(f'Найдено фамилий: {len(surnames)}')
print(f'Уникальных фамилий: {len(unique)}')

new_text = re.sub(r'\bроман\b', 'произведение', text, flags=re.IGNORECASE)

with open('writer_modified.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)
