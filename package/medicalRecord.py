class medicalRecord():
    records =[]

    def __init__(self, patientId, test, date, result, unit, status,resultDate = None):
        self.patientId = patientId
        self.test = test
        self.date = date
        self.result = result
        self.unit = unit
        self.status = status
        if resultDate != None:
            self.resultDate = resultDate

    def updateRecord(self, testName=None, result=None, status=None, resultsDate=None):
        if testName:
            self.testName = testName
        if result:
            self.result = result
        if status:
            self.status = status
        if resultsDate:
            self.resultsDate = resultsDate


    def addPatient(self,patient):
        self.patient = patient


    def addTest(self,test):
        self.test = test

    def addDate(self,date):
        self.date = date

    def addResult(self,result):
        self.result = result