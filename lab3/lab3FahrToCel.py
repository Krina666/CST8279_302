#This program will convert Fahrenheit to Celsius.
#Coded by : Changqi Li
#Last Modified: Oct 3 , 2020

TempStr = input("Please enter a temperature value with a symbol：")
print("The temperature value you entered is" + TempStr)

if TempStr[-1] in ["F","f"]:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("The converted temperature is{:.2f}C".format(C))

elif TempStr[-1] in ["C","c"]:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("The converted temperature is{:.2f}F".format(F))
