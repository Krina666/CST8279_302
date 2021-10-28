def function():
    us = float(input("Please enter the us$: "))
    if not(bool(user)):
        ca = us * 1.31
    else:
        ca = us * float(user)
    print('can$ is : ' + str(ca))

    restart = input("Would you want to start the program again yes or no")
    if(restart == "yes"):
        function()

def isfloat():
    split_rate = []
    split_rate = user.split(".")
    if len(split_rate) == 2 and split_rate[0] and split_rate[1].isdigit():
        return True
    return False

user = input("Please enter the exchange rate")

while not(isfloat()) and bool(user):
    user = input("Please enter the exchange rate")
    #update user input
function()










