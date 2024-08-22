from . import medicalRecord as mrClass, MedicalTest
from . import validityCheck as validCheck
from . import MedicalTest as mtClass

medicalTests = []
medicalRecords = []


# main 5 tests


def medicalTestsSetUP():
    with open("medicalTest.txt", 'w') as file:
        # Opening the file in write mode will clear its contents
        pass

    testHgb = mtClass("Hemoglobin", "Hgb", (13.8, 17.2), "g/dL", "00-03-04")
    testHgb.addMedicalTest(testHgb.numberOfMedicalTests)

    testBGT = mtClass("Blood Glucose Test", "BGT", (70, 99), "mg/dL", "00-12-06")
    testBGT.addMedicalTest(testBGT.numberOfMedicalTests)
    testLDL = mtClass("LDL Cholesterol Low-Density Lipoprotein", "LDL", (0, 100), "mg/dL", "00-17-06")
    testLDL.addMedicalTest(testLDL.numberOfMedicalTests)
    testsystole = mtClass("Systolic Blood Pressure", "systole", (0, 120), "mm Hg", "00-08-04")
    testsystole.addMedicalTest(testsystole.numberOfMedicalTests)
    testdiastole = mtClass("Diastolic Blood Pressure", "diastole", (0, 80), "mm Hg", "00-10-00")
    testdiastole.addMedicalTest(testdiastole.numberOfMedicalTests)

    listOfMainTests = [testHgb, testBGT, testLDL, testsystole, testdiastole]

    for i in listOfMainTests:
        medicalTests.append(i)


# Usage
medicalTestsSetUP()


def addNewMedicalTest():
    print("Adding new medical test :")
    print("Enter the name of the medical test:")
    name = input()

    print("Enter the abbreviation of the medical test:")
    abbreviation = input()

    print(
        "Enter the min normal range of the medical test:(The range should be positive, if there is no min range enter -1 )")
    min_range = input()
    print(
        "Enter the max normal range of the medical test: (The range should be positive, if there is no max range enter -1 )")
    max_range = input()

    test_range = [min_range, max_range]

    print("Enter the unit for this medical test:")
    unit = input()

    print("Enter the time to be completed for this medical test: (Form : DD-hh-mm)")
    time_to_be_completed = input()
    medical_test = mtClass(name, abbreviation, test_range, unit, time_to_be_completed)

    medical_test.addMedicalTest(MedicalTest.numberOfMedicalTests)

    print(medical_test.getAbbreviation(), "is added successfully to medical tests")


def addNewMedicalRecord():
    print("Enter the patient ID")
    patient_id = input()
    while not validCheck.validPatientID(patient_id):
        print("Wrong Patient ID, please try again")
        patient_id = input()

    print("Enter the test abbreviation")
    test_abbreviation = input()
    while not validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
        print("Wrong Test Abbreviation, please try again")
        test_abbreviation = input()

    for test in medicalTests:
        if test.getAbbreviation() == test_abbreviation:
            patient_medical_test = test

    print("Enter the date of the test (YYYY-MM-DD hh:mm)")
    date = input()
    while not validCheck.validDate(date):
        print("Wrong Date of Test, please try again")
        date = input()

    print("Enter your test result")
    result = input()
    while not validCheck.validResult(result):
        print("Wrong Medical Record, please try again")
        result = input()

    print("Enter the record status")
    status = input()
    while not validCheck.validStatus(status):
        print("Wrong Record Status, please try again")
        status = input()

    unit = validCheck.getUnit(medicalTests, test_abbreviation)

    medical_record = mrClass.MedicalRecord(patient_id, patient_medical_test, date, result, unit, status)
    medicalRecords.append(medical_record)
    medical_record.addToMedicalRecord()
    # write into medicalRecord.txt print(patientID)

    print("Added Successfully")
    return



def updateMedicalRecord():
    patient_id = input("Enter the patient ID: ")
    test_abbreviation = input("Enter the test abbreviation: ")

    for record in medicalRecords:
        if record.patient_id == patient_id and record.test.getAbbreviation() == test_abbreviation:
            new_status = input("Enter new status: ")
            new_result = input("Enter new result: ")

            record.updateRecord(result=new_result, status=new_status)
            print("Record updated successfully")
            return

    print("Record not found.")


def updateMedicalTest():
    test_name = input("Enter the name of the medical test to update: ")
    new_range = input("Enter the new range for the test (min,max): ")
    min_range, max_range = map(int, new_range.split(','))

    for test in medicalTests:
        if test.getTestName() == test_name:
            test.updateMedicalTest(test_name, [min_range, max_range])
            print(f"Medical test '{test_name}' updated successfully.")
            return

    print(f"Medical test '{test_name}' not found.")

def filterMedicalRecords():
    tempList=[]
    while True:
        print("Choose the categories you would like to filter: ")
        print("1. Patient ID")
        print("2. Test Name")
        print("3. Abnormal Test")
        print("4. Specific Date")
        print("5. Test Status")
        print("6. Test turnaround time")#didnt make a function for that one
        print("7. Exit Filter")
        choice = int(input())
        if choice == 1:
            patient_id = int(input("Enter the patient ID: "))
            if validCheck.validPatientID(patient_id):
                if not tempList:
                    for record in medicalRecords:
                        if record.patientID == patient_id:
                            tempList.append(record)
                else:
                    for record in tempList:
                        if record.patientID != patient_id:
                            tempList.remove(record)
            else:
                continue

        elif choice==2:
            test_name = int(input("Enter test name: "))
            if validCheck.validTestAbbreviation(medicalTests, test_name):
                if tempList == []:
                    for record in medicalRecords:
                        if record.testName == test_name:
                            tempList.append(record)
                else:
                    for record in tempList:
                        if record.testName != test_name:
                            tempList.remove(record)
            else:
                print("Invalid testName")

        elif choice==3:
            if tempList == []:
                for record in medicalRecords:
                    if validCheck.upNormalResult(mtClass.medicalTestNames, record.test_range, mtClass.medicalTestAbbreviations):
                        tempList.append(record)
            else:
                for record in tempList:
                    if not validCheck.upNormalResult(mtClass.medicalTestNames, record.test_range, mtClass.medicalTestAbbreviations):
                        tempList.remove(record)


        elif choice==4:
            start_date=input("Enter the start date of search (YYYY-MM-DD): ")
            finish_date=input("Enter the end date of search (YYYY-MM-DD): ")
            if validCheck.validDate(start_date) and validCheck.validDate(finish_date):
                if tempList == []:
                    for record in medicalRecords:
                        if record.date >= start_date and record.date <= finish_date:
                            tempList.append(record)
                else:
                    for record in tempList:
                        if record.date >= start_date and record.date <= finish_date:
                            tempList.remove(record)
            else:
                continue

        elif choice==5:
            test_status = int(input("Enter test status: "))
            if validCheck.validStatus(test_status):
                if tempList == []:
                    for record in medicalRecords:
                        if record.status == test_status:
                            tempList.append(record)
                else:
                    for record in tempList:
                        if record.status != test_status:
                            tempList.remove(record)
            else:
                continue

        elif choice==6:
            return #empty so no errors pop up

        elif choice==7:
            for record in tempList:
                print(record)
            print("Exiting filter...")
            return


def filterMedicalTests():
    print("Choose the categories you would like to filter: ")
    print("1. Test Abbreviation")
    print("2. Range")
    print("3. Unit of Test")
    print("4. Execution Time")
    choice = int(input())

    if choice == 1:
        test_abbreviation = input("Enter the test abbreviation: ")
        if validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
            for test in medicalTests:
                if test.getAbbreviation() == test_abbreviation:
                    print(mtClass.printMedicalTest(test))
        else:
            print("No such test abbreviation")

    elif choice == 2:
        first_input = input("Range is greater than or equal to (Leave empty if there is no lower limit): ")
        second_input = input("Range is less than or equal to (Leave empty if there is no upper limit): ")

        first_test_range = float(first_input) if first_input else float('-inf')
        second_test_range = float(second_input) if second_input else float('inf')

        for test in medicalTests:
            test_range = test.getRange()
            if first_test_range <= test_range[0] and second_test_range >= test_range[1]:
                print(mtClass.printMedicalTest(test))

    elif choice == 3:
        unit = input("Enter the unit: ")
        for test in medicalTests:
            if test.getUnit() == unit:
                print(mtClass.printMedicalTest(test))

    elif choice == 4:
        print("Choose a filter for execution time:")
        print("1. More than a certain time")
        print("2. Less than a certain time")
        print("3. Equal to a certain time")
        sub_choice = int(input())

        execution_time = input("Enter the execution time (dd:hh:mm): ")
        execution_minutes = time_to_minutes(execution_time)

        if execution_minutes is not None:  # Proceed only if the time format is valid
            for test in medicalTests:
                test_minutes = time_to_minutes(test.getTimeToBeCompleted())

                if test_minutes is not None:  # Ensure that test_minutes is valid
                    if sub_choice == 3 and test_minutes == execution_minutes:
                        print(mtClass.printMedicalTest(test))
                    elif sub_choice == 2 and test_minutes < execution_minutes:
                        print(mtClass.printMedicalTest(test))
                    elif sub_choice == 1 and test_minutes > execution_minutes:
                        print(mtClass.printMedicalTest(test))
        else:
            print("Invalid time format entered.")


def time_to_minutes(time_str):
    try:
        # Split the string by colon and convert to integers
        days, hours, minutes = map(int, time_str.split(':'))
        return days * 24 * 60 + hours * 60 + minutes
    except ValueError:
        # Handle the case where the format is incorrect
        print(f"Error: Invalid time format '{time_str}'. Expected format is 'dd:hh:mm'.")
        return None

def deleteMedicalRecord():
        tempList=[]
        choice=int(input("How would you like to delete a record: "))
        print("1. Patient ID")
        print("2. Test Name")
        print("3. Specific Date")
        print("4. Test Status")
        if choice==1:
            patient_id = int(input("Enter the patient ID: "))
            if validCheck.validPatientID(patient_id):
                for record in medicalRecords:
                    if record.patientID == patient_id:
                        tempList.append(record)
                if tempList == []:
                    print("No such patient")
                    return
                else:
                    for record in tempList:
                        print(record)
                    tempList=[]
                second_choice=input("what test name would you like to delete: ")
                for record in tempList:
                    if record.testName == second_choice:
                        medicalRecords.remove(record)
            else:
                print("That's not a valid patient ID")
                return

        elif choice==2:
            test_name = input("Enter test name you want to delete from the records: ")
            for record in medicalRecords:
                if record.testName == test_name:
                    medicalRecords.remove(record)

        elif choice==3:
            start_date = input("Enter the start date of delete (YYYY-MM-DD): ")
            finish_date = input("Enter the end date of delete (YYYY-MM-DD): ")
            if validCheck.validDate(start_date) and validCheck.validDate(finish_date):
                for record in medicalRecords:
                    if record.date >= start_date and record.date <= finish_date:
                        medicalRecords.remove(record)
            else:
                    print("That's not a valid date range")
                    return
        elif choice==4:
            status = input("Enter test status: ")
            if validCheck.validStatus(status):
                for record in medicalRecords:
                    if record.status == status:
                        medicalRecords.remove(record)
            else:
                print("That's not a valid test status")
                return

#def deleteMedicalTest():
    #test_abbreviation=input("Enter the test Abbreviation you want to delete: ")
    #if validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
       # for record in medicalRecords:
      #      if record.abbreviation == test_abbreviation:
     #           medicalRecords.remove(record)
    #else:
        #print("That's not a valid test abbreviation")


def generateTextualSummary():
    with open("summary_report.txt", "w") as file:
        for record in medicalRecords:
            file.write(f"Patient ID: {record.patient_id}, Test: {record.test.getAbbreviation()}, Date: {record.date}, "
                       f"Result: {record.result} {record.unit}, Status: {record.status}\n")

    print("Summary report generated")


def exportMedicalRecords():
    import csv

    with open('medical_records_export.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Patient ID', 'Test', 'Date', 'Result', 'Unit', 'Status'])

        for record in medicalRecords:
            writer.writerow([record.patient_id, record.test.getAbbreviation(), record.date, record.result,
                             record.unit, record.status])

    print("Medical records exported successfully to 'medical_records_export.csv'")



def importMedicalRecords():
    import csv

    with open('medical_records_import.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            patient_id, test_abbreviation, date, result, unit, status = row

            for test in medicalTests:
                if test.getAbbreviation() == test_abbreviation:
                    patient_medical_test = test

            medical_record = mrClass.MedicalRecord(patient_id, patient_medical_test, date, result, unit, status)
            medicalRecords.append(medical_record)

    print("Medical records imported successfully from 'medical_records_import.csv'")
