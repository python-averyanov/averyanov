#1. Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?
from pickle import GLOBAL

listy = []
def PR4():#создали функцию
    try:
        a = input("введите число   ")
        kol = 0
        while True:
            c = str(a)
            for i in c:
                listy.append(int(i))
            b = sum(listy)
            kol = kol + 1  # подсчет количества выполнений цикла
            a = int(a) - b
            listy.clear()
            print("количество выполнений цикла:", kol)  # выводим
            print("____________________________________")
            if int(a) > 0:  # если 'а' больше 0, продолжаем
                continue
            else:
                break
    except ValueError:
        print("вы ввели не число")
        PR4()

PR4()

