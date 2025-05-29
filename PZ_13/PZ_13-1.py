# 1. Перенести в новый двумерный список Matr1 элементы, которые не находятся в
# первых и последних строках и столбцах матрицы Matr2 произвольного размера.
# 2. В двумерном списке отрицательные элементы возвести в квадрат.
import random


listy = list(list(random.randint(-10,10) for i in range(4))for i in range(3))
print(listy)

inr = listy[1:-1]
print(inr)
print('новая матрица: ',a := list(map(lambda row: row[1:-1], inr)))
print(f'отрицательные элементы в квадрате:', list(map(lambda r: list(map(lambda x: x**2 if x < 0 else x, r)),a)))

