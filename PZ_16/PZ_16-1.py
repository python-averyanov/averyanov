class circle:
    def __init__(self, r):
        self.r = r

    def ploshad(self):
        return 3.14 * self.r ** 2

    def long(self):
        return 2 * 3.14 * self.r

    def twor(self):
        return 2 * self.r

c = circle(12345678999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
print(c.ploshad())