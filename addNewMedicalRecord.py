import validityCheck
print("Enter the patient ID")
patientID = int(input())
if validityCheck.validPatientID(patientID):
    print("valid")
