#Create a switch for a number

floor_number = 4

match floor_number:
    case 4:
        print("Unlucky in Japan")
    case 13:
        print("Unlucly in America")
    case _:
        print("No issues with this floor number :D")