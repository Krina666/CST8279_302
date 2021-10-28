import csv
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


def updateCsv():
    rows = []
    with open("final302.csv", "r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row:
                rows.append(row)

    for row in rows[2:]:
        row[5] = calculateDecimalGrade(float(row[2]), float(row[3]), float(row[4]))
        row[6] = calculateAlphabeticalGrade(row[5])
        row[5] = "%.2f" % row[5]
    with open("final302.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(rows)


updateCsv()