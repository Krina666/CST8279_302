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

def calculateAlphabeticalGrade(DecGrade):
    #Set default value if empty
    if not bool(DecGrade) and DecGrade != 0.0:
        DecGrade = 67.0
    if DecGrade >= 90:
        return 'A+'
    elif DecGrade >= 85:
        return 'A'
    elif DecGrade >= 80:
        return 'A-'
    elif DecGrade >= 77:
        return 'B+'
    elif DecGrade >= 73:
        return 'B'
    elif DecGrade >= 70:
        return 'B-'
    elif DecGrade >= 67:
        return 'C+'
    elif DecGrade >= 63:
        return 'C'
    elif DecGrade >= 60:
        return 'C-'
    else:
        return 'F'



ValToTest = [[50.0, 60.0, 70.0], [63.0, 34.0, 33.0], [90.0, 34.0, 23.0], [90.0, 82.0, 100.0]]
for i in ValToTest:
    Decimal = calculateDecimalGrade(i[0], i[1], i[2])
    Alpha = calculateAlphabeticalGrade(Decimal)
    print("Decimal is: ", Decimal, "AlphabeticalGrade is: ", Alpha)