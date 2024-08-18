

class MedicalTest:
    numberOfMedicalTests = 0
    def __init__(self, testName, abbreviation, range, unit, addedDate):
        self.testName = testName
        self.abbreviation = abbreviation
        self.range = range
        self.unit = unit
        self.addedDate = addedDate
        MedicalTest.numberOfMedicalTests += 1

    def addMedicalTest(self, numberOfMedicalTests):
        openMedicalTestFile=open("medicalTest.txt", "a")
        openMedicalTestFile.write(f"{numberOfMedicalTests}. Name: {self.testName} ({self.abbreviation}); Range: {self.range}; Unit: {self.unit}, {self.addedDate}\n")

    def printMedicalTest(self):
        print(self.testName, self.abbreviation, self.range, self.unit, self.addedDate)

    def updateMedicalTest(self, testName, newRange):
        readMedicalTests= open("medicalTest.txt", "r")
        lines = readMedicalTests.readlines()

        writeMedicalTest =open("medicalTest.txt", "w")
        for line in lines:
            if line.startswith(testName):
                parts = line.strip().split(',')
                parts[2] = newRange
                writeMedicalTest.write(','.join(parts) + '\n')
            else:
                writeMedicalTest.write(line)


def deleteMedicalTest(self, testName):
    readMedicalTest= open("medicalTest.txt", "r")
    lines = readMedicalTest.readlines()
    writeMedicalTest= open("medicalTest.txt", "w")
    for line in lines:
        if not line.startswith(testName):
            writeMedicalTest.write(line)

