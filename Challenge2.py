#Add a parent or a child class

import random

class Shape:
    side = 1 

class Square(Shape):
    sides = 4

    def area(self):
        return self.height * self.height
        
my_shape = Square()
my_shape.height = 10
print(my_shape.area())