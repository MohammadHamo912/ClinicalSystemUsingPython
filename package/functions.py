from . import medicalRecord as mrClass
from . import validityCheck as validCheck
from . import MedicalTest as mtClass

medicalTests = []
medicalRecords = []


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
    while not validCheck.validPatientID(medicalTests,patient_id):
        print("Wrong Patient ID, please try again")
        patient_id = input()

    print("Enter the test abbreviation")
    test_abbreviation = input()
    while not validCheck.validTestAbbreviation(test_abbreviation):
        print("Wrong Test Abbreviation, please try again")
        test_abbreviation = input()

    print("Enter the date of the test (YYYY-MM-DD hh:mm)")
    date = input()
    while not validCheck.validDate(date):
        print("Wrong Date of Test, please try again")
        date = input()

    print("Enter the medical record")
    result = input()
    while not validCheck.validResult(result):
        print("Wrong Medical Record, please try again")
        result = input()

    print("Enter the record status")
    status = input()
    while not validCheck.validResult(status):
        print("Wrong Record Status, please try again")
        status = input()

    unit = validCheck.getUnit(medicalTests, test_abbreviation)

    medical_record = mrClass.MedicalRecord(patient_id, test_abbreviation, date, result, unit, status)
    medicalRecords.append(medical_record)
    medical_record.writeToMedicalRecordtxt()
    # write into medicalRecord.txt print(patientID)

    print("Added Successfully")
    return
