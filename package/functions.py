from . import medicalRecord as mrClass, MedicalTest
from . import validityCheck as validCheck
from . import MedicalTest as mtClass

medicalTests = []
medicalRecords = []


# main 5 tests


def medicalSystemSetUP():
    with open('medicalTest.txt', 'w') as medicalTests:
        medicalTests.write("")

    with open('medicalRecord.txt', 'w') as medicalRecords:
        medicalRecords.write("")
    importMedicalTests()
    importMedicalRecords()

# Usage

def medicalSystemShutDown():
    exportMedicalTests()
    exportMedicalRecords()



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
    medicalTests.append(medical_test)
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
    while True:
        try:
            if validCheck.validDate(date):
                print("Valid Date")
                break
            else:
                print("Invalid Date")
                date = input()
        except ValueError:
            print("Invalid date ")
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
                    print(test)
        else:
            print("No such Test abbreviation")

    if choice == 2:
        first_test_range = float(input("Range is greater than or equal to: "))
        second_test_range = float(input("Range is less than or equal to: "))
        for test in medicalTests:
            if test.getrange()[0] == first_test_range and test.getrange()[1] == second_test_range:
                print(test)

    if choice == 3:
        unit=input("Enter the unit: ")
        for test in medicalTests:
            if test.getUnitOfTest() == unit:
                print(test)

    if choice == 4:
        print("Choose a choice")
        print("1. More than a certain time")
        print("2. Less than a certain time")
        print("3. equal to a certain time")
        choice = int(input())
        if choice == 3:
            execution_time = input("Enter the execution time (dd:hh:mm): ")
            for test in medicalTests:
                if test.getExecutionTime() == execution_time:
                    print(test)

        elif choice == 2:
            execution_time = input("Enter the max execution time (dd:hh:mm): ")
            for test in medicalTests:
                if test.getExecutionTime() < execution_time:
                    print(test)

        elif choice == 1:

            execution_time = input("Enter the min execution time (dd:hh:mm): ")
            for test in medicalTests:
                if test.getExecutionTime() > execution_time:
                    print(test)

        else:
            print("Invalid choice")


def deleteMedicalRecord():
        tempList=[]
        print("How would you like to delete a record: ")
        print("1. Patient ID")
        print("2. Test Name")
        print("3. Specific Date")
        print("4. Test Status")
        choice = int(input())

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

        else :
            print("Invalid Choice")
            return

def deleteMedicalTest():
    test_abbreviation=input("Enter the test Abbreviation you want to delete: ")
    if validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
        for record in medicalRecords:
            if record.abbreviation == test_abbreviation:
                medicalRecords.remove(record)
    else:
        print("That's not a valid test abbreviation")


def generateTextualSummary():
    with open("summary_report.txt", "w") as file:
        for record in medicalRecords:
            file.write(f"Patient ID: {record.patient_id}, Test: {record.test.getAbbreviation()}, Date: {record.date}, "
                       f"Result: {record.result} {record.unit}, Status: {record.status}\n")

    print("Summary report generated")


def exportMedicalRecords():
    import csv

    with open('medical_records.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Patient ID', 'Test', 'Date', 'Result', 'Unit', 'Status'])

        for record in medicalRecords:
            writer.writerow([record.patient_id, record.test.getAbbreviation(), record.date, record.result,
                             record.unit, record.status])

    print("Medical records exported successfully to 'medical_records.csv'")



def importMedicalRecords():
    import csv

    with open('medical_records.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            patient_id, test_abbreviation, date, result, unit, status = row

            for test in medicalTests:
                if test.getAbbreviation() == test_abbreviation:
                    patient_medical_test = test

            medical_record = mrClass.MedicalRecord(patient_id, patient_medical_test, date, result, unit, status)
            medicalRecords.append(medical_record)
            medical_record.addToMedicalRecord()
    print("Medical records imported successfully from 'medical_records_import.csv'")





def importMedicalTests():
    import csv
    import ast

    with open('medical_tests.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row

        for row in reader:
            test_name, test_abbreviation, temp_test_range, test_unit, test_date = row
            test_range = ast.literal_eval(temp_test_range)

            medical_test = mtClass(test_name, test_abbreviation, test_range, test_unit, test_date)
            medicalTests.append(medical_test)
            medical_test.addMedicalTest(mtClass.numberOfMedicalTests)




def exportMedicalTests():
    import csv

    with open('medical_tests.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Abbreviation','Range', 'Unit', 'Date'])

        for test in medicalTests:
            writer.writerow([test.test_name, test.abbreviation,test.test_range, test.unit, test.time_to_be_completed])
