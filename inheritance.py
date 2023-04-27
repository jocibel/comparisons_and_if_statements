import random

class Animal:
    info = "a living organism that feeds on organic matter"

    def __init__(self, name):
        print("An animal is created")
        self.name = name

class Dog(Animal):
    info = "A furry animal."

    def __init__(self, name):
        super().__init__(name)
        print("A dog is created")
        self.lucky_number = (random.randint(1,10))
        self.fur = ""

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}") 


class Bulldog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("A bulldog is created")

dog1 = Bulldog("Jack")

