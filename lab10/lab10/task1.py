import os

f = open("2000_GirlsNames.txt", "r")
f2 = open("2000_GirlsNames.csv", "w")
fb = open("2000_BoysNames.txt", "r")
fb2 = open("2000_BoyNames.csv", "w")
f2.write("First name,Count\n")
fb2.write("First name,Count\n")


def function(openfile, outfile):
    while True:
        line = openfile.readline()

        # print(type(line))

        if line == "":
            break
        if line.find(" ") > 0:
            # for i in line:
            #    if i == " ":
            line2 = line.replace(" ", ",", 1)
            # Only return a copy, do not modify the original string
            outfile.write(line2)
            print(line2)
            continue


function(f, f2)
function(fb, fb2)

f.close()
f2.close()
fb.close()
fb2.close()
