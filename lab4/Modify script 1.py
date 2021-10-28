import random

yesorno = True
while yesorno:

    user = input("Please enter a number")
    while not(user.isnumeric()):
        user = input("Please enter a number")
    numberoffaces = int(user)

    while numberoffaces < 1 or numberoffaces > 24:
        numberoffaces = int(input('Please enter a number'))
        print (numberoffaces)
    generatedValue = random.randint(1, numberoffaces)
    print("Your value is {}".format(generatedValue))

    yesorno = input("Would you want to start rolling again yes or no")
    if (yesorno == "yes"):
        yesorno = True
    else:
        yesorno = False











