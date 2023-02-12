# Im this we have seen about the operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # here we are doing Point of summmation as if we not do this it will return as a string
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}x+{self.y}y"


point1 = Point(9, 5)
point2 = Point(1, 4)
print(point1)
print(point2)
print(point1 + point2)
