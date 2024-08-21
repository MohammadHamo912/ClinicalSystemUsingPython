
class Patient:
    patientsIDs = []
    medicalRecords = []
    def __init__(self,id):
        self.id = id
        Patient.patiensIDs.append(id)

    def addPatientRecord(self):
        from ClinicalSystemUsingPython.package import functions
        medicalRecord = functions.addNewMedicalRecord()
        Patient.medicalRecords.append(medicalRecord)

    def updatePatientRecord(self, testName, updateData):
        for record in self.medicalRecords:
            if record.testName == testName:
                record.updateRecord(**updateData)
            else:
                print("record not found")
    def deleteTest(self, testName):
        self.medicalRecords = [record for record in self.medicalRecords if record.testName != testName]

    def getTest(self, testName):
        for record in self.medicalRecords:
            if record.testName == testName:
                return record
        print("test Not found")
        return None



