import medicalRecord as mR
import validityCheck as vc

def addNewMedicalRecords():
    print("Enter the patient ID")
    patientID = input()
    while not vc.validPatientID(patientID):
        print("Wrong Patient ID, please try again")
        patientID = input()


    print("Enter the test name")
    testName = input()
    while not vc.validTestName(testName):
        print("Wrong Test Name, please try again")
        testName = input()

    print("Enter the date of the test")
    date = input()
    result = input()
    unit = input()
    status = input()



    #contiue reading

    medicalRecord = mR(patientID,testName,date,result,unit,status)

    # write into medicalRecord.txtprint(patientID)
    return medicalRecord

def addNewMeidcalTest(test):
    print(test)



