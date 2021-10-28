
def function():
    F = float(input("Please enter the Tempreture in Fajrenheit: "))
    C = (F - 32)//1.8
    print("The Tempreture in Celsius is: " + str(C))

    restart = input('Would you want to start the program again yes or no')
    if (restart == "yes"):
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