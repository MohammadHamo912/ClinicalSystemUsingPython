# replace the test_abbreviation with the object test and show its abbreviation as an identity

class MedicalRecord:
    records = []

    def __init__(self, patient_id, test, date, result, unit, status):
        self.patient_id = patient_id
        self.test = test
        self.date = date
        self.result = result
        self.unit = unit
        self.status = status
        if status == "Completed":
            self.result_date = self.test.getTimeToBeCompleted()
        else:
            self.result_date = None

    def updateRecord(self, test=None, result=None, status=None, result_date=None):
        if test:
            self.test = test
        if result:
            self.result = result
        if status:
            self.status = status
        if result_date:
            self.result_date = result_date

    def addToMedicalRecord(self):
        with open("medicalRecord.txt", 'a') as file:
            record = f"{self.patient_id}: {self.test.getAbbreviation()}, {self.date}, {self.result}, {self.unit}, {self.status}"
            if self.result_date:
                record += f", {self.result_date}"
            record += "\n"
            file.write(record)


        file.close()
