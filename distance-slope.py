import math

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        p1 = (x2 - x1) ** 2
        p2 = (y2 - y1) ** 2
        return (p1 + p2) ** 0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        p1 = (y2 - y1)
        p2 = (x2 - x1)
        return p1 / p2

li = Line((3,2), (8,10))
print(li.distance())
print(li.slope())
