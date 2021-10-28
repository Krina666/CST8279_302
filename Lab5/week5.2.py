def displayInstructions2(programer="Changqi Li",thisDate="Oct 22 2020"):
    print("This program will find the Max of three numbers")
    print("You will need to enter three numbers and then compare which one is the maximum")
    print("It was coded in Python by {}".format(programer))
    print("Last modified {}".format(thisDate))

displayInstructions2(programer="Changqi Li",thisDate="Oct 22 2020")

number1 = int(input("Please enter the first number"))
number2 = int(input("Please enter the second number"))
number3 = int(input("Please enter the third number"))

def numberMax(n1,n2,n3):
    n = 0
    if n1 > n2:
        n = n1
    else:
        n = n2
    if n > n3:
        return "The max value is: " + str(n)
    else:
        n = n3
        return "The max value is: " + str(n)

Max = numberMax(number1,number2,number3)
print(Max)