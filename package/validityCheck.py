def validPatientID(patiendID):
    if len(patiendID) != 7:
        return False
    for num in patiendID:
        if not num.isdigit():
            return False
    return True


def validTestName(testName):
    openMedicalTest=open("medicalTest.txt", "r")
    for line in openMedicalTest:
        if testName in line:
            return True
    return False

def upNormalResult(testResult, testName):
    if not validTestName():
        print("Invalid test name")
        return
    openMedicalTest = open("medicalTest.txt", "r")
    for line in openMedicalTest:
        if testName in line: # 2. Name: Blood Glucose Test (BGT); Range: > 70, < 99; Unit: mg/dL, 00-12-06
#                              3. Name: LDL Cholesterol Low-Density Lipoprotein (LDL); Range: < 100; Unit: mg/dL, 00-17-06

            parts = line.split(";")
            if len(parts) >= 2:
                range_part = parts[1].strip().split(",")
                minVal = float(range_part[0].strip().split("> ")[1])
                maxVal = float(range_part[1].strip().split("< ")[1])
            if testResult >= minVal and testResult <= maxVal:
                return False
            else:
                return True




def validDate(date):
    yearMonthDay, time = date.split()

    year, month, day = map(int, yearMonthDay.split('-'))
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    hour, minute = map(int, time.split(':'))
    if not (0 <= hour <= 23):
        return False
    if not (0 <= minute <= 59):
        return False

    return True

