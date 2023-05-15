file = open("cheese.txt", "r")

#file_text = file.read()
#print(file_text)

#lines = file.readlines()
#print(lines)

for line in file:
    print(line)
    
file.close()

# Create a file numbers.txt that has a few lines of numbers.
# Multiply all the numbers together and print the result.

with open("numbers.txt", "r") as file:
    total = 1
    for line in file:
        try:
            number = float(line.strip())
            total *= number
        except ValueError:
            pass

print(total)
