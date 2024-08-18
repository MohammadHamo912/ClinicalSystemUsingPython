class MedicalTest:
    numberOfMedicalTests = 0
    medicalTestNames = []
    medicalTestAbbreviations = []

    def __init__(self, test_name, abbreviation, test_range, unit, time_to_be_completed):
        self.testName = test_name
        self.abbreviation = abbreviation
        self.range = test_range
        self.unit = unit
        self.addedDate = time_to_be_completed
        MedicalTest.numberOfMedicalTests += 1
        MedicalTest.medicalTestNames.append(test_name)
        MedicalTest.medicalTestAbbreviations.append(abbreviation)

    def addMedicalTest(self, numberOfMedicalTests):
        open_medical_test_file = open("medicalTest.txt", "a")
        open_medical_test_file.write(
            f"{numberOfMedicalTests}. Name: {self.testName} ({self.abbreviation}); Range: {self.range}; Unit: {self.unit}, {self.addedDate}\n")

    def printMedicalTest(self):
        print(self.testName, self.abbreviation, self.range, self.unit, self.addedDate)

    def updateMedicalTest(self, testName, newRange):
        read_medical_tests = open("medicalTest.txt", "r")
        lines = read_medical_tests.readlines()

        write_medical_test = open("medicalTest.txt", "w")
        for line in lines:
            if line.startswith(testName):
                parts = line.strip().split(',')
                parts[2] = newRange
                write_medical_test.write(','.join(parts) + '\n')
            else:
                write_medical_test.write(line)

    def deleteMedicalTest(self, testName):
        readMedicalTest = open("medicalTest.txt", "r")
        lines = readMedicalTest.readlines()
        writeMedicalTest = open("medicalTest.txt", "w")
        for line in lines:
            if not line.startswith(testName):
                writeMedicalTest.write(line)

    def getAbbreviation(self):
        return self.abbreviation

    def getUnit(self):
        return self.unit


# writing the first 5 main tests


testHgb = MedicalTest("Hemoglobin", "Hgb", (13.8, 17.2), "g/dL", "00-03-04")
testHgb.addMedicalTest(testHgb.numberOfMedicalTests)

testBGT = MedicalTest("Blood Glucose Test", "BGT", (70, 99), "mg/dL", "00-12-06")
testBGT.addMedicalTest(testBGT.numberOfMedicalTests)
testLDL = MedicalTest("LDL Cholesterol Low-Density Lipoprotein", "LDL", (0, 100), "mg/dL", "00-17-06")
testLDL.addMedicalTest(testLDL.numberOfMedicalTests)
testsystole = MedicalTest("Systolic Blood Pressure", "systole", (0, 120), "mm Hg", "00-08-04")
testsystole.addMedicalTest(testsystole.numberOfMedicalTests)
testdiastole = MedicalTest("Diastolic Blood Pressure", "diastole", (0, 80), "mm Hg", "00-10-00")
testdiastole.addMedicalTest(testdiastole.numberOfMedicalTests)
