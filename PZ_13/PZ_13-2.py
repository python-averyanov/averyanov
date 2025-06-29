# 2. В двумерном списке отрицательные элементы возвести в квадрат.
import random

listy = list(list(random.randint(-10,10) for i in range(5))for i in range(5))
print(listy)

listy = (lambda j: list(map(lambda x:x**2 if x < 0 else x,j)),listy)
print(list(listy))
