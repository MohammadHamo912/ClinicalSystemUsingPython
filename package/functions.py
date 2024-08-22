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

    print("Added Successfully")
    return



def updateMedicalRecord():
    patient_id = input("Enter the patient ID: ")
    test_abbreviation = input("Enter the test abbreviation: ")
    date = input("Enter the test Date")
    result = input("Enter the record result")
    status = input("Enter the record status")

    for record in medicalRecords:
        if (record.patient_id == patient_id and record.test.getAbbreviation() == test_abbreviation
                and record.date == date and record.result == result and record.status == status):

            print("Enter the new patient ID: (or enter nothing if you dont want to change)")
            new_patient_id = input()
            if new_patient_id == None:
                new_patient_id = patient_id
            else:
                while not validCheck.validPatientID(new_patient_id):
                    print("Wrong Patient ID, please try again")
                    new_patient_id = input()


            print("Enter the new record test's abbreviation (or enter nothing if you dont want to change)")
            new_test_abbreviation = input()
            if new_test_abbreviation == None:
                new_test_abbreviation = test_abbreviation
            else:
                while not validCheck.validTestAbbreviation(medicalTests, new_test_abbreviation):
                    print("Wrong Test Abbreviation, please try again")
                    new_test_abbreviation = input()

                for test in medicalTests:
                    if test.getAbbreviation() == test_abbreviation:
                        patient_medical_test = test

            print("Enter the date of the updated test (YYYY-MM-DD hh:mm)(or enter nothing if you dont want to change)")
            new_date = input()
            if new_date == None:
                new_date = date
            else:
                while True:
                    try:
                        if validCheck.validDate(date):
                            print("Valid Date")
                            break
                        else:
                            print("Invalid Date")
                            new_date = input()
                    except ValueError:
                        print("Invalid date ")
                        new_date = input()




            print("Enter your updated test result (or enter nothing if you dont want to change)")
            new_result = input()
            if new_result == None:
                new_result = result

            else:

                while not validCheck.validResult(new_result):
                    print("Wrong Medical Record, please try again")
                    new_result = input()

            print("Enter the record status (or enter nothing if you dont want to change)")
            new_status = input()
            if new_status == None:
                new_status = status
            else:
                while not validCheck.validStatus(status):
                    print("Wrong Record Status, please try again")
                    new_status = input()


            unit = validCheck.getUnit(medicalTests, new_test_abbreviation)
            record.setPatientID(new_patient_id)
            record.setTest(patient_medical_test)
            record.setDate(new_date)
            record.setResult(new_result)
            record.setStatus(new_status)


            medicalRecords.append(record)
            break

            exportMedicalRecords()


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
    tempList = medicalRecords[:]

    while True:
        print("Choose the categories you would like to filter: ")
        print("1. Patient ID")
        print("2. Test Name")
        print("3. Abnormal Test")
        print("4. Specific Date")
        print("5. Test Status")
        print("6. Test turnaround time")  # Function not implemented yet
        print("7. Exit Filter")
        choice = int(input())

        if choice == 1:
            patient_id = input("Enter the patient ID: ")
            if validCheck.validPatientID(patient_id):
                tempList = [record for record in tempList if record.patient_id == patient_id]
            else:
                print("Invalid patient ID.")
                continue

        elif choice == 2:
            test_name = input("Enter test name: ")
            if validCheck.validTestAbbreviation(medicalTests, test_name):
                tempList = [record for record in tempList if record.test_name == test_name]
            else:
                print("Invalid test name.")
                continue

        elif choice == 3:
            tempList = [record for record in tempList if validCheck.upNormalResult(mtClass.medicalTestNames, record.result, mtClass.medicalTestAbbreviations)]

        elif choice == 4:
            start_date = input("Enter the start date of search (YYYY-MM-DD): ")
            end_date = input("Enter the end date of search (YYYY-MM-DD): ")
            if validCheck.validDate(start_date) and validCheck.validDate(end_date):
                tempList = [record for record in tempList if start_date <= record.date <= end_date]
            else:
                print("Invalid date format.")

        elif choice == 5:
            test_status = input("Enter test status: ")
            if validCheck.validStatus(test_status):
                tempList = [record for record in tempList if record.status == test_status]
            else:
                print("Invalid test status.")
                continue

        elif choice == 6:
            print("Test turnaround time filtering not implemented yet.")
            continue

        elif choice == 7:
            if tempList:
                for record in tempList:
                    print(record)
            else:
                print("No records match the selected criteria.")
            print("Exiting filter...")
            return

        else:
            print("Invalid choice. Please try again.")


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
        #case1 ( both empty ) Done
        #case2 ( first empty, the second not empty ) Done
        #case3 ( first not empty, the second empty ) Not Done ( no result is displayed)
        #case4 ( both not empty ) Not Done ( just the first one is displayed)
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

        execution_time = input("Enter the execution time (dd-hh-mm): ")
        execution_minutes = time_to_minutes(execution_time)

        if execution_minutes is not None:
            for test in medicalTests:
                test_minutes = time_to_minutes(test.getTimeToBeCompleted())

                if test_minutes is not None:
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
        days, hours, minutes = map(int, time_str.split('-'))
        return days * 24 * 60 + hours * 60 + minutes
    except ValueError:
        print(f"Error: Invalid time format '{time_str}'. Expected format is 'dd-hh-mm'.")
        return None

def deleteMedicalRecord(medicalRecords):
        tempList=[]
        print("How would you like to delete a record: ")
        print("1. Patient ID")
        print("2. Test Name")
        print("3. Specific Date")
        print("4. Test Status")
        choice = int(input())

        if choice == 1:
            patient_id = int(input("Enter the patient ID: "))
            if validCheck.validPatientID(patient_id):
                tempList = [record for record in medicalRecords if record.patient_id == patient_id]
                if not tempList:
                    print("No such patient")
                    return
                else:
                    for record in tempList:
                        print(record)

                    second_choice = input("What test name would you like to delete: ")

                    updated_records = [record for record in medicalRecords if not (record.patient_id == patient_id and record.testName == second_choice)]
                    medicalRecords = updated_records
            else:
                print("That's not a valid patient ID")
                return

        elif choice == 2:
            test_name = input("Enter test name you want to delete from the records: ")
            for record in medicalRecords:
                if record.testName == test_name:
                    medicalRecords.remove(record)

        elif choice == 3:
            start_date = input("Enter the start date of delete (YYYY-MM-DD): ")
            finish_date = input("Enter the end date of delete (YYYY-MM-DD): ")
            if validCheck.validDate(start_date) and validCheck.validDate(finish_date):
                for record in medicalRecords:
                    if record.date >= start_date and record.date <= finish_date:
                        medicalRecords.remove(record)
            else:
                    print("That's not a valid date range")
                    return
        elif choice == 4:
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
        for test in medicalTests:
            if test.abbreviation == test_abbreviation:
                medicalTests.remove(test)
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
