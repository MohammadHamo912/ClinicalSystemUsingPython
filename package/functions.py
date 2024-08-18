import medicalRecord as mR


def addNewMedicalRecords():
    print("Enter the patient ID")
    patientID = int(input())
    testName = input()
    date = input()
    result = input()
    unit = input()
    status = input()



    #contiue reading

    medicalRecord = mR(patientID,testName,date,result,unit,status)

    return medicalRecord
    print(patientID)

def addNewMeidcalTest(test):
    print(test)



