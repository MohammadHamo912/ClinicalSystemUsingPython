from . import medicalRecord as mrClass
from . import validityCheck as validCheck
from . import MedicalTest as mtClass

medicalTests = []
medicalRecords = []


# main 5 tests


def medicalTestsSetUP():
    with open("medicalTest.txt", 'w') as file:
        # Opening the file in write mode will clear its contents
        pass

    testHgb = mtClass("Hemoglobin", "Hgb", (13.8, 17.2), "g/dL", "00-03-04")
    testHgb.addMedicalTest(testHgb.numberOfMedicalTests)

    testBGT = mtClass("Blood Glucose Test", "BGT", (70, 99), "mg/dL", "00-12-06")
    testBGT.addMedicalTest(testBGT.numberOfMedicalTests)
    testLDL = mtClass("LDL Cholesterol Low-Density Lipoprotein", "LDL", (0, 100), "mg/dL", "00-17-06")
    testLDL.addMedicalTest(testLDL.numberOfMedicalTests)
    testsystole = mtClass("Systolic Blood Pressure", "systole", (0, 120), "mm Hg", "00-08-04")
    testsystole.addMedicalTest(testsystole.numberOfMedicalTests)
    testdiastole = mtClass("Diastolic Blood Pressure", "diastole", (0, 80), "mm Hg", "00-10-00")
    testdiastole.addMedicalTest(testdiastole.numberOfMedicalTests)

    listOfMainTests = [testHgb, testBGT, testLDL, testsystole, testdiastole]

    for i in listOfMainTests:
        medicalTests.append(i)


# Usage
medicalTestsSetUP()


def addNewMedicalTest():
    print("Adding new medical test :")
    print("Enter the name of the medical test:")
    name = input()

    print("Enter the abbreviation of the medical test:")
    abbreviation = input()

    print("Enter the min normal range of the medical test:")
    min_range = input()
    print("Enter the max normal range of the medical test:")
    max_range = input()

    test_range = (min_range, max_range)

    print("Enter the unit for this medical test:")
    unit = input()

    print("Enter the time to be completed for this medical test: (Form : DD-hh-mm)")
    time_to_be_completed = input()
    medical_test = mtClass(name, abbreviation, test_range, unit, time_to_be_completed)

    medicalTests.append(medical_test)

    print(medical_test.getAbbreviation(), "is added successfully to medical tests")


def addNewMedicalRecord():
    print("Enter the patient ID")
    patient_id = input()
    while not validCheck.validPatientID(patient_id):
        print("Wrong Patient ID, please try again")
        patient_id = input()

    print("Enter the test abbreviation")
    test_abbreviation = input()
    while not validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
        print("Wrong Test Abbreviation, please try again")
        test_abbreviation = input()

    print("Enter the date of the test (YYYY-MM-DD hh:mm)")
    date = input()
    while not validCheck.validDate(date):
        print("Wrong Date of Test, please try again")
        date = input()

    print("Enter your test result")
    result = input()
    while not validCheck.validResult(result):
        print("Wrong Medical Record, please try again")
        result = input()

    print("Enter the record status")
    status = input()
    while not validCheck.validStatus(status):
        print("Wrong Record Status, please try again")
        status = input()

    unit = validCheck.getUnit(medicalTests, test_abbreviation)

    medical_record = mrClass.MedicalRecord(patient_id, test_abbreviation, date, result, unit, status)
    medicalRecords.append(medical_record)
    medical_record.addToMedicalRecord()
    # write into medicalRecord.txt print(patientID)

    print("Added Successfully")
    return
