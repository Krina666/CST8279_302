import math as m

def function():
    radius = float(input('Please enter the radius of the circle: '))
    area = m.pi * pow(radius,2)
    print('The area of circle is:' + str(area))

    restart = input('Would you want to start the program again yes or no')
    if (restart == 'yes'):
      function()

def isfloat():
    split_value = []
    split_value = user.split(".")
    if len(split_value) == 2 and split_value[0] and split_value[1].isdigit():
        return True
    return False

user = input("Please enter a value: ")

while not(isfloat()):
    user = input("Please enter a value: ")

function()