# with open('text18-1.txt', 'r', encoding="utf=16") as file:
#     lines = file.readlines()
# print(a := ''.join(lines)) #1
#
# a2 = list(filter(str.isupper,a))
# print(f"количество заглавных букв {len(a2)}") #2
#
# print(lines)
#
# fin = [lines[1]] + [lines[-1]] + lines[1:]
# print(fini := ''.join(fin)) #3
#
# with open('new_file11.txt','w',encoding='utf=16') as file2:
#     file2.write(fini)


#напишите программу, которая копирует содержимое файла "example.txt" в новый файл "сopy_example.txt"
#если исходного файла не сущенствует, программа должна вывести сообщение о ошибке

with open('example.txt', 'w') as f:
    f.write('dsfsdfsdfsfsfsfsdfsdf')
    


