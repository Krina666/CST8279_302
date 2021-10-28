import random

def displayInstructions2(programer="Changqi Li",thisDate="Oct 22 2020"):
    print("This program will simulates the rolling of a dice.")
    print("You will enter the number of faces of a dice as a parameter, and then roll the dice.")
    print("It was coded in Python by {}".format(programer))
    print("Last modified {}".format(thisDate))
displayInstructions2(programer="Changqi Li",thisDate="Oct 22 2020")

number = int(input("Please enter a number: "))
number_f = int(number)

def Rollthedice(p):
    result = random.randint(1, p)
    print("Your value is {}".format(result))

Rollthedice(number_f)
