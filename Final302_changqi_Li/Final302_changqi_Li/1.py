def calculateDecimalGrade(Assign, MT, FP):
    #Set default value if empty
    if not bool(Assign) and Assign != 0.0:
        Assign = 50
    if not bool(MT) and Assign != 0.0:
        MT = 60
    if not bool(FP) and Assign != 0.0:
        FP = 100

    DecGrade = 0.35*MT + 0.4*Assign + 0.25*FP
    return(DecGrade)

print(calculateDecimalGrade(50, 60, 70))
print(calculateDecimalGrade(63, 34, 33))
print(calculateDecimalGrade(90, 34, 23))
print(calculateDecimalGrade(90, 82, 100))

