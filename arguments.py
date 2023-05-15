import sys

total = 1
args = sys.argv[1:]
for argument in args:
    try:
        number = float(argument)
        total *= number
    except ValueError as e:
        print("Only numbers can be provided")
        sys.exit(1)

print(total)

