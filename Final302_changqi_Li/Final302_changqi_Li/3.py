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



