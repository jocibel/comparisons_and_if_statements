import random

class Square:
    sides = 4

    def area(self):
        return self.height * self.height
        
my_shape = Square()
my_shape.height = 10
print(my_shape.area())
