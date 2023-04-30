#Challenge 
#Use reduce to multiply all the number together

numbers = [1,2,3,4,5]

from functools import reduce

big_number = reduce(lambda total, number: number * total, numbers)

print(big_number)