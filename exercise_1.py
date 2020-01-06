import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self, radius):
        return (2 * math.pi * radius)

    def area(self, radius):
        area = radius * radius
        return(math.pi * area)
