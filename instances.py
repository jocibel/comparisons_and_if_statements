import random

class Bowl:
    info = "A round glossy glass bowl with red trimming letters"


    def __init__(self, name):
        print("I'm round!")
        self.lucky_number = (random.randint(1,10))
        self.name = name

bowl1 = Bowl("Jack")
bowl2 = Bowl("Cookie")


print(bowl1.name)
print(bowl2.name)
