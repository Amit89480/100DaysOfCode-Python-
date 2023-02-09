class shape:
    def __init__(self, x, y):
        self.x = x;
        self.y = y

    def squareArea(self):
        return self.x * self.y




class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)

    # Here we are overriding the function of parents class shape and implementing it to areaCicle function
    def AreaCircle(self):
        return 3.14 * super().squareArea()


c1 = Circle(5)
print(c1.AreaCircle())
