class Rectangle_:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def returnArea(self):
        area = (self.length * self.width)
        return area

Cuboid1 = Rectangle_(70,60)
print(Cuboid1.returnArea())