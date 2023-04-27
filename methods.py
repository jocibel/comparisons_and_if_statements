import random

class Dog:
    info = "A furry animal."


    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = (random.randint(1,10))
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}") 

dog1 = Dog("Jack")
dog2 = Dog("Cookie")


dog1.bark()
dog2.bark()