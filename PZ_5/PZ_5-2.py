#2. Описать функцию PowerA234(параметры), вычисляющую вторую, третью и
#четвертую степень числа A и возвращающую эти степени соответственно в
#переменные B, C и D. С помощью этой функции найти вторую, третью и четвертую
#степень пяти данных чисел.
def powerA234(A):#создали функцию
    B = A ** 2
    C = A ** 3
    D = A ** 4
    return B, C, D


for i in range(1,6):#выполнится 5 раз
   try:
      k = int(input("введи число"))# вводим число
   except ValueError:
       print("минус попытка")
       continue
   B, C, D, = powerA234(k)
   print("вторая степень", B)
   print("третья степень", C)
   print("четвертая степень", D)


