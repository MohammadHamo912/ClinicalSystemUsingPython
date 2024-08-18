# replace the test_abbreviation with the object test and show its abbreviation as an identity

class MedicalRecord:
    records = []

    def __init__(self, patient_id, test_abbreviation, date, result, unit, status, result_date=None):
        self.patient_id = patient_id
        self.test_abbreviation = test_abbreviation
        self.date = date
        self.result = result
        self.unit = unit
        self.status = status
        if result_date is not None:
            self.result_date = result_date
        else:
            self.result_date = None
    def updateRecord(self, test_abbreviation=None, result=None, status=None, result_date=None):
        if test_abbreviation:
            self.test_abbreviation = test_abbreviation
        if result:
            self.result = result
        if status:
            self.status = status
        if result_date:
            self.result_date = result_date

    def addToMedicalRecord(self):
        with open("medicalRecord.txt", 'a') as file:
            record = f"{self.patient_id}: {self.test_abbreviation}, {self.date}, {self.result}, {self.unit}, {self.status}"
            if self.result_date:
                record += f", {self.result_date}"
            record += "\n"
            file.write(record)

        file.close()
