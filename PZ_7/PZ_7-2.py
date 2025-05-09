#. Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}».
#Если скобки расставлены правильно (то есть каждой открывающей соответствует
#закрывающая скобка того же вида), то вывести число 0. В противном случае
#вывести или номер позиции, в которой расположена первая ошибочная скобка,
#или, если закрывающих скобок не хватает, число —1.

def che(s: str) -> int:
    round = 0
    square = 0
    curly = 0

    for i, char in enumerate(s):

        if char == '(':
            round += 1
        elif char == ')':
            if round == 0:
                return i + 1
            round -= 1

        elif char == '[':
            square += 1
        elif char == ']':
            if square == 0:
                return i + 1
            square -= 1

        elif char == '{':
            curly += 1
        elif char == '}':
            if curly == 0:
                return i + 1
            curly -= 1

    if round > 0:
        return s.index('(') + 1
    if square > 0:
        return s.index('[') + 1
    if curly > 0:
        return s.index('{') + 1

    return 0  # Все правильно

# Ввод строки
s = input("Введите строку: ")
print(che(s))