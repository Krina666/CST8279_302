#This program will generate a random value
#Coded by : Changqi Li
#Last Modified: Oct 3 , 2020
#Algorithm:

import random

numberofFaces = input("Please enter the number of faces of your dice (Max 10)?>>")
numberofFaces = int(numberofFaces)

if ( numberofFaces > 10):
    print("New number")
else:
    generatedValue = random.randint(1, numberofFaces)
    print("Your value is {}".format(generatedValue))

print("The computer generated the value {}".format(generatedValue),"on a dice with", numberofFaces, "faces.")








