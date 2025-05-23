from abc import ABC, abstractmethod
import math

#Abstract base class
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        return area


shape = Circle(radius=5)
print("area of a circle is :",shape.calculate_area())

shape = Rectangle(10, 5)
print("Area of a Rectangle is : ", shape.calculate_area())