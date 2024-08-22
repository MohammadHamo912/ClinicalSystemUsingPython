def validPatientID(patient_id):
    patient_id = str(patient_id)
    if len(patient_id) != 7:
        return False
    for num in patient_id:
        if not num.isdigit():
            return False
    return True


def validTestAbbreviation(medical_tests, abbreviation):
    for abb in medical_tests:
        if abb.getAbbreviation() == abbreviation:
            return True
    return False


def upNormalResult(medical_tests, test_result, test_abbreviation):
    if not validTestAbbreviation(medical_tests, test_abbreviation):
        print("Invalid test name")
        return
    open_medical_test = open("medicalTest.txt", "r")
    for test in medical_tests:
        if test_abbreviation == test.getAbbreviation:
            test_range = test.getRange()
            min_val = test_range[0]
            max_val = test_range[1]
            if min_val <= test_result <= max_val:
                return False
            else:
                return True


def validDate(date):
    try:
        if ' ' in date:
            yearMonthDay, time = date.split()
        else:
            yearMonthDay = date
            time = ''

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

        if time:
            hour, minute = map(int, time.split(':'))
            if not (0 <= hour <= 23):
                return False
            if not (0 <= minute <= 59):
                return False

        return True
    except ValueError:
        return False


# this needs edit
def validResult(result):
    for num in result:
        if not num.isdigit():
            return False
    return True


def validStatus(status):
    if status == "Pending" or status == "Completed" or status == "Reviewed":
        return True
    return False


def getUnit(medicalTests, testAbbreviation):
    for test in medicalTests:
        if testAbbreviation == test.getAbbreviation():
            return test.getUnit()

    return
