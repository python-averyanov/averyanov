#1. Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые
#числа, расположенные между A и B (включая сами числа A и B), а также количество
#N этих чисел
try:
   a = int(input("введите число    "))# вводим числа
   b = int(input("введите число больше первого    "))
   if a < b:
      listy = [a]  # создаем список
      while a < b:  # пока а меньше 'б'
          a = a + 1  # добавляем к 'а' единицу
          listy.append(a)  # добавляем 'а' в конец списка
          print(a)  # при помощи len считаем количество символов в списке
      print("количество: ",len(listy))
   else:
       print("первое число больше второго")
except ValueError: # Если что то идет не так, используем заготовленные переменные
    print("вы ввели не число")
