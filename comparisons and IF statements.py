
age = 23
height = 162

#and
if age >= 23 and height >= 162:
    print("You can ride the ride!")


#or
if age >= 17 or height >= 170:
    print("You can ride the super ride!")


#elif (else if)
if height < 162:
    print("You can't ride any rides :()")
elif height < 170:
    print("You can ride level-1 rides") 
elif height < 200:
    print("You can ride any ride at the park!")
else:
    print("Too tall to ride the rides :()")