#2. Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено
#максимально возможное количество квадратов со стороной C (без наложений).
#Найти количество квадратов, размещенных на прямоугольнике. Операции
#умножения и деления не использовать.

try:
   a = int(input('сторона а  '))# вводим числа
   b = int(input('сторона b  '))
   c = int(input('сторона квадрата  '))
except ValueError:# Если что то идет не так, используем заготовленные переменные
    a = 10
    b = 23
    c = 3

high = 0
widht = 0
while a >= c:# считаем, сколько квадратов можно разместить по высоте
    a -= c
    high += 1

while b >= c:#тоже самое, только с шириной
    b -= c
    widht += 1

squares = 0
for _ in range(high):#считаем результат
    squares += widht
print(squares)


