# READ
# file = open("cheese.txt", "r")
# lines = file.readlines()
# file.close()

# # EDIT
# lines.insert(0, "I like cheese\n")  # Make sure to add a newline character at the end of the line
# lines[1] = "Hello!\n"
# lines[-1] = lines[-1] + "\n"
# lines.append("Goodbye!")

# # WRITE
# file = open("cheese.txt", "w")
# file.writelines(lines)
# file.close()

# #Multiply each of the numbers in number.txt by 2
# READ
with open("numbers.txt", "r") as file:
    lines = file.readlines()

# EDIT
for x in range(len(lines)):
    try:
        number = float(lines[x].strip()) * 2
        lines[x] = f"{number}\n"
    except ValueError:
        pass

# WRITE
with open("numbers.txt", "w") as file:
    file.write("I like numbers.\n")
    file.writelines(lines)

# CALCULATE TOTAL
total = 1
for line in lines:
    try:
        number = float(line.strip())
        total *= number
    except ValueError:
        pass

print(total)





