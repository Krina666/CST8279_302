import csv

f = input("File name:")
file = open(f)
fi = file.readlines() #return type 'string' without s, type 'list' with s
print(fi)
file.close()


#2000_GirlsNames.csv


