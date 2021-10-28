# This program will generate an exchange rate conversio.
# Coded by : Changqi Li.
#Last Modified: Oct 3 , 2020

# The exchange rate of US for CAN is: 1US = 2CAN.
# Define the exchange rate function.
def exchange_money(in_money, ex_rate):
    out_money = in_money * ex_rate
    return out_money


money_value = input("Please enter the money value: ")

money_num_value = eval(money_value)

unit = input("Please enter the unit of currency you want to convert（US/CAN：")

if unit == "CAN":
    exchange_rate = 1 / 2

elif unit == "US":
    exchange_rate = 2

out_money = exchange_money(money_num_value, exchange_rate)

print("The converted amount is：", out_money)