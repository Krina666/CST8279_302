gradeDict = {}

f = open("final302.csv", "r")
while True:
    line = f.readline()
    if line == "":
        break
    if line.find(" "):
        pass
    elif line.find(","):
        line = line.split(",")
        #line[0]+line[1] is the concatenation of names, line[5] and line[6] are decimal and letter grades respectively.
        gradeDict[line[0]+line[1]] = [line[5], line[6]]

count = True
while count:
    name = input("please enter the full name of a student without space(i.e. MariaInce) or q to quit:")
    if name == "q":
        exit()
    try:
        print("The student is: ", name, "; decimal grade is: ", gradeDict[name][0], "; Alphabetical Final grade is: ", gradeDict[name][1])
        count = False
    except KeyError:
        print("The student is not in the dictionary")

f.close()