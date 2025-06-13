# Создайте класс "Фигура", который содержит метод расчета площади фигуры.
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
class Figura:
    pass


class Square(Figura):
    def __init__(self,side):
        self.side = side

    def one(self):
        return self.side ** 2



class Long_square(Figura):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def one(self):
        return self.width * self.height

a = Square(12)
print(a.one())