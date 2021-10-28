def displayInstructions3(programer="Changqi Li",thisDate="Oct 22 2020"):
    print("This program will calculate the factorial")
    print("You will need to enter a non-negative integer for calculation")
    print("It was coded in Python by {}".format(programer))
    print("Last modified {}".format(thisDate))

displayInstructions3(programer="Changqi Li",thisDate="Oct 22 2020")

number = int(input("Please enter the non-negative integer: "))

def number_value(n):
    if n == 0:
        return 1
    else:
        return n * number_value(n-1)

result = number_value(n=number)
print(result)