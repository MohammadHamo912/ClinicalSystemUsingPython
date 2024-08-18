class MedicalTest:
    numberOfMedicalTests = 0
    medicalTestNames = []
    medicalTestAbbreviations = []

    def __init__(self, test_name, abbreviation, test_range, unit, time_to_be_completed):
        self.testName = test_name
        self.abbreviation = abbreviation
        self.test_range = test_range
        self.unit = unit
        self.time_to_be_completed = time_to_be_completed
        MedicalTest.numberOfMedicalTests += 1
        MedicalTest.medicalTestNames.append(test_name)
        MedicalTest.medicalTestAbbreviations.append(abbreviation)

    def addMedicalTest(self, numberOfMedicalTests):
        open_medical_test_file = open("medicalTest.txt", "a")
        open_medical_test_file.write(
            f"{numberOfMedicalTests}. Name: {self.testName} ({self.abbreviation}); Range: {self.test_range}; Unit: {self.unit}, {self.time_to_be_completed}\n")

    def printMedicalTest(self):
        print(self.testName, self.abbreviation, self.test_range, self.unit, self.time_to_be_completed)

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

    def getRange(self):
        return self.test_range


