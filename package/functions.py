
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
        "Enter the min normal range of the medical test:(The range should be positive, if there is no min range enter 0 )")
    min_range = float(input())
    while (min_range < 0):
        print("the range should be positive, if there is no min range enter 0")
        min_range = float(input())

    print(
        "Enter the max normal range of the medical test: (The range should be positive, if there is no max range enter 0 )")
    max_range = float(input())

    while (max_range < 0 or (max_range < min_range and max_range != 0)):
        print("the max range should be positive and bigger than the min range, if there is no max range enter 0")
        max_range = float(input())

    test_range = [min_range, max_range]

    print("Enter the unit for this medical test:")
    unit = input()

    print("Enter the time to be completed for this medical test: (Form : DD-hh-mm)")
    time_to_be_completed = input()
    #check the validity for this

    medical_test = mtClass(name, abbreviation, test_range, unit, time_to_be_completed)

    medical_test.addMedicalTest()
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
                break
            else:
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
    for record in medicalRecords:
        if (
                record.patient_id == patient_id and record.test.getAbbreviation() == test_abbreviation and record.date == date and record.result == result
                and record.status == status):
            print("This record already exists")
            return
    medical_record = mrClass.MedicalRecord(patient_id, patient_medical_test, date, result, unit, status)
    medicalRecords.append(medical_record)
    medical_record.addToMedicalRecord()

    print("Added Successfully")
    return


def updateMedicalRecord():
    tempList = medicalRecords.copy()

    # Print all records
    for record in medicalRecords:
        print(record)

    # Get and validate patient ID
    patient_id = input("Enter the patient ID: ")
    while not validCheck.validPatientID(patient_id):
        print("Wrong Patient ID, please try again.")
        patient_id = input("Enter the patient ID: ")

    # Filter records by patient ID
    tempList = [record for record in tempList if record.patient_id == patient_id]

    # If no records found, exit early
    if not tempList:
        print("No records found for the given patient ID.")
        return

    # Print filtered records
    for record in tempList:
        print(record)

    # Get and validate additional details
    test_abbreviation = input("Enter the test abbreviation: ")
    while not validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
        print("Wrong Test Abbreviation, please try again")
        test_abbreviation = input("Enter new Test Abbreviation: ")

    date = input("Enter the test Date (YYYY-MM-DD hh:mm): ")
    while not validCheck.validDate(date):
        print("Wrong Test Date, please try again")
        date = input("Enter new Test Date: ")
    # Search for the specific record
    for record in medicalRecords:
        if (record.patient_id == patient_id and
                record.test.getAbbreviation() == test_abbreviation and
                record.date == date):

            while True:
                print("What do you want to update in the record: ")
                print("1. Patient ID")
                print("2. Test abbreviation")
                print("3. Test date")
                print("4. Test result")
                print("5. Status")
                print("6. Exit")
                choice = input("Enter your choice: ")

                # Collect new details based on user choice
                if choice == "1":
                    new_patient_id = input("Enter new Patient ID: ")
                    while not validCheck.validPatientID(new_patient_id):
                        print("Wrong Patient ID, please try again")
                        new_patient_id = input("Enter new Patient ID: ")
                    record.setPatientID(new_patient_id)


                elif choice == "2":
                    new_test_abb = input("Enter new Test abbreviation: ")
                    while not validCheck.validTestAbbreviation(medicalTests, new_test_abb):
                        print("Wrong Test Abbreviation, please try again")
                        new_test_abb = input("Enter new Test Abbreviation: ")

                    for test in medicalTests:
                        if test.getAbbreviation() == new_test_abb:
                            record.setTest(test)

                    changeResultDate(record)

                elif choice == "3":
                    new_date = input("Enter new Test date (YYYY-MM-DD hh:mm): ")
                    while not validCheck.validDate(new_date):
                        print("Wrong Test Date, please try again")
                        new_date = input("Enter new Test date: ")
                    record.setDate(new_date)
                    changeResultDate(record)

                elif choice == "4":
                    new_result = input("Enter new Test result: ")
                    while not validCheck.validResult(new_result):
                        print("Wrong Test Result, please try again")
                        new_result = input("Enter new Test result: ")
                    record.setResult(new_result)


                elif choice == "5":
                    new_status = input("Enter new Test status: ")
                    while not validCheck.validStatus(new_status):
                        print("Wrong Test Status, please try again")
                        new_status = input("Enter new Test status: ")
                    record.setStatus(new_status)
                    changeResultDate(record)


                elif choice == "6":
                    break
                else:
                    print("Invalid choice, please try again.")

            # Save updates to persistent storage
            exportMedicalRecords()
            print("Record updated successfully.")
            return

    print("Record not found.")


def updateMedicalTest():
    i =1
    for test in medicalTests:
        print(f"{i}. ",end="")
        test.printMedicalTest()
        i +=1

    test_name = input("Enter the Abbreviation of the medical test you want to update: ")

    for test in medicalTests:
        if test.getAbbreviation() == test_name:
            print("Enter a new test Name ( or enter 0 if you dont want to change )")
            name = input()
            if name == "0":
                name = test.getTestName()

            print("Enter a new test abbreviation: ( or press enter if you dont want to change ) ")
            abbreviation = input()
            while (abbreviation != None and validCheck.validTestAbbreviation(medicalTests,abbreviation)):
                print("this abbreviation already exists enter another abbreviation ( or enter 0if you dont want to change ) ")
                abbreviation = input()
            if abbreviation == "0":
                abbreviation = test.getAbbreviation()


            print ("If you want to change the test range enter 1 or enter 0 if you dont want to change")
            temp = input()

            if temp == "1":
                print("Enter new min range for the test")
                min_range = input()
                try:
                    while min_range < 0:
                        print("The range should be positive or enter 0 if you dont want a min range")
                        min_range = input()
                except:
                    print("The range should be in numeric numbers only")


                print("Enter a new max range for the test")
                max_range = input()
                try:
                    while max_range < 0 or max_range < min_range:
                        print("The range should be positive and bigger than min range or enter 0 if you dont want to put a max range")
                        max_range = input()
                except:
                    print("The range should be in numeric numbers only")
            else :
                min_range = test.getRange()[0]
                max_range = test.getRange()[1]

            test_range = [min_range, max_range]

            print("Enter a new unit for the test( or enter 0 if you dont want to change )")
            unit = input()
            if unit == "0":
                unit = test.getUnit()

            print("Enter the time to be completed for this medical test: (Form : DD-hh-mm) ( or enter 0 if you dont want to change )")
            time_to_be_completed = input()
            if(time_to_be_completed == "0"):
                time_to_be_completed = test.getTimeToBeCompleted()


            test.updateMedicalTest(name,abbreviation,test_range,unit,time_to_be_completed)

            print(f"Medical test '{test_name}' updated successfully.")
            return

    print(f"Medical test '{test_name}' not found.")


def filterMedicalRecords():
    tempList = [medicalRecords,[],[],[],[],[],[]]
    i =0
    while True:
        print("Choose the categories you would like to filter: ")
        print("1. Patient ID")
        print("2. Test Name")
        print("3. UpNormal Test")
        print("4. Specific Date")
        print("5. Test Status")
        print("6. Test turnaround time")  # Function not implemented yet
        print("7. show all medical records")
        print("8. Exit Filter")
        choice = input()

        if choice == ("1"):
            patient_id = input("Enter the patient ID: ")
            if validCheck.validPatientID(patient_id):
                for record in tempList[i]:
                    if record.patient_id == patient_id:
                        tempList[i+1].append(record)
                        print(record)

            else:
                print("Invalid patient ID.")
                continue

        elif choice == "2":
            test_name = input("Enter test name: ")
            if validCheck.validTestAbbreviation(medicalTests, test_name):
                for record in tempList[i]:
                    if record.test.getAbbreviation() == test_name:
                        tempList[i + 1].append(record)
                        print(record)
            else:
                print("Invalid test abbreviation.")
                continue

        elif choice == "3":
            for record in tempList[i]:
                if validCheck.upNormalResult(medicalTests, float(record.result), record.test.getAbbreviation()):
                    tempList[i + 1].append(record)
                    print(record)


        elif choice == "4":
            from datetime import datetime

            start_date = input("Enter the start date of search (YYYY-MM-DD): ")
            date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            start_date = date_obj.strftime("%Y-%m-%d %H:%M")
            end_date = input("Enter the end date of search (YYYY-MM-DD): ")
            date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            end_date = date_obj.strftime("%Y-%m-%d %H:%M")

            if validCheck.validDate(start_date) and validCheck.validDate(end_date):
                for record in tempList[i]:
                    if start_date <= record.date <=end_date:
                        tempList[i + 1].append(record)
                        print(record)
            else:
                print("Invalid date format.")

        elif choice == "5":
            test_status = input("Enter test status: ")
            if validCheck.validStatus(test_status):
                for record in tempList[i]:
                    if record.status == test_status:
                        tempList[i + 1].append(record)
                        print(record)
            else:
                print("Invalid test status.")
                continue

        elif choice == "6":
            from datetime import datetime

            start_date = input("Enter the start date of search (YYYY-MM-DD): ")
            date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            start_date = date_obj.strftime("%Y-%m-%d %H:%M")
            end_date = input("Enter the end date of search (YYYY-MM-DD): ")
            date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            end_date = date_obj.strftime("%Y-%m-%d %H:%M")

            if validCheck.validDate(start_date) and validCheck.validDate(end_date):
                for record in tempList[i]:
                    if(record.status == "Completed"):
                        if start_date <= record.result_date <= end_date:
                            tempList[i + 1].append(record)
                            print(record)
            else:
                print("Invalid date format.")




        elif choice == "7":
            for record in medicalRecords:
                print(record)


        elif choice == "8":
            print("Exiting filter...")
            tempList = [medicalRecords, [], [], [], []]
            return

        else:
            print("Invalid choice. Please try again.")

        i+=1


def filterMedicalTests():
    print("Choose the categories you would like to filter: ")
    print("1. Test Abbreviation")
    print("2. Range")
    print("3. Unit of Test")
    print("4. Execution Time")
    print("5. All medical tests")
    print("6. exit")
    choice = input()


    if choice == "1":
        test_abbreviation = input("Enter the test abbreviation: ")
        if validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
            for test in medicalTests:
                if test.getAbbreviation() == test_abbreviation:
                    print(test.printMedicalTest())
        else:
            print("No such test abbreviation")

    elif choice == "2":
        first_input = input("Range is greater than or equal to (Leave empty if there is no lower limit): ")
        second_input = input("Range is less than or equal to (Leave empty if there is no upper limit): ")

        first_test_range = float(first_input) if first_input else float(0)
        second_test_range = float(second_input) if second_input else float(0)

        for test in medicalTests:
            test_range = test.getRange()
            if (first_test_range <= test_range[0] and second_test_range >= test_range[1]):
                print(test.printMedicalTest())

    elif choice == "3":
        unit = input("Enter the unit: ")
        for test in medicalTests:
            if test.getUnit() == unit:
                print(test.printMedicalTest())

    elif choice == "4":
        print("Choose a filter for execution time:")
        print("1. More than a certain time")
        print("2. Less than a certain time")
        print("3. Equal to a certain time")
        sub_choice = input()

        execution_time = input("Enter the execution time (dd-hh-mm): ")
        execution_minutes = time_to_minutes(execution_time)

        if execution_minutes is not None:
            for test in medicalTests:
                test_minutes = time_to_minutes(test.getTimeToBeCompleted())

                if test_minutes is not None:
                    if sub_choice == "3" and test_minutes == execution_minutes:
                        print(test.printMedicalTest())
                    elif sub_choice == "2" and test_minutes < execution_minutes:
                        print(test.printMedicalTest())
                    elif sub_choice == "1" and test_minutes > execution_minutes:
                        print(test.printMedicalTest())
        else:
            print("Invalid time format entered.")

    elif choice == "5":
        for test in medicalTests:
            print(test.printMedicalTest())

    elif choice == "6":
        return

    else:
        print("wrong choice")


def time_to_minutes(time_str):
    try:
        days, hours, minutes = map(int, time_str.split('-'))
        return days * 24 * 60 + hours * 60 + minutes
    except ValueError:
        print(f"Error: Invalid time format '{time_str}'. Expected format is 'dd-hh-mm'.")
        return None


def deleteMedicalRecord():
    print("How would you like to delete a record:")
    print("1. Patient ID")
    print("2. Test Name")
    print("3. Specific Date Range")
    print("4. Test Status")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        patient_id = input("Enter the patient ID: ").strip()
        tempList = [record for record in medicalRecords if record.patient_id == patient_id]

        if not tempList:
            print(f"No records found for patient ID '{patient_id}'.")
            return

        print("Records found:")
        for record in tempList:
            print(record)

        test_name = input(
            "Enter the test name you would like to delete (or press Enter to delete all records for this patient): ").strip().lower()

        if test_name:
            matching_records = [record for record in tempList if record.test.getAbbreviation().lower() == test_name]
            if not matching_records:
                print(f"No records found for test name '{test_name}' for patient ID '{patient_id}'.")
                return

            print("The following records will be deleted:")
            for record in matching_records:
                print(record)

            confirm = input("Are you sure you want to delete these records? (yes/no): ").strip().lower()
            if confirm == "yes":
                medicalRecords[:] = [record for record in medicalRecords if not (
                        record.patient_id == patient_id and record.test.getAbbreviation().lower() == test_name)]
                print("Records have been deleted.")
            else:
                print("Deletion canceled.")
        else:
            confirm = input(
                f"Are you sure you want to delete all records for patient ID '{patient_id}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                medicalRecords[:] = [record for record in medicalRecords if record.patient_id != patient_id]
                print("All records for this patient have been deleted.")
            else:
                print("Deletion canceled.")


    elif choice == '2':
        test_name = input("Enter the test name you want to delete from the records: ").strip().lower()
        updated_records = [record for record in medicalRecords if record.test.getAbbreviation().lower() != test_name]
        medicalRecords[:] = updated_records
        print(f"Records with test name '{test_name}' have been deleted.")

    elif choice == '3':
        start_date = input("Enter the start date for deletion (YYYY-MM-DD): ").strip()
        finish_date = input("Enter the end date for deletion (YYYY-MM-DD): ").strip()

        try:
            updated_records = [record for record in medicalRecords if
                               not (start_date <= record.date.split(' ')[0] <= finish_date)]
            medicalRecords[:] = updated_records
            print(f"Records between dates '{start_date}' and '{finish_date}' have been deleted.")
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")

    elif choice == '4':
        status = input("Enter the test status: ").strip().lower()
        updated_records = [record for record in medicalRecords if record.status.lower() != status]
        medicalRecords[:] = updated_records
        print(f"Records with status '{status}' have been deleted.")

    else:
        print("Invalid Choice.")
        return

    print("Deletion completed. Updated records:")
    for record in medicalRecords:
        print(record)


def deleteMedicalTest():
    test_abbreviation = input("Enter the test Abbreviation you want to delete: ")
    if validCheck.validTestAbbreviation(medicalTests, test_abbreviation):
        print ("Deleting the medical test will lead to delete all the records for it")
        confirm = input("Are you sure you want to delete this test? (yes/no): ").strip().lower()
        if confirm == "yes":

            updated_records = [record for record in medicalRecords if
                               record.test.getAbbreviation().lower() != test_abbreviation]
            medicalRecords[:] = updated_records
            print(f"Records with test name '{test_abbreviation}' have been deleted.")

            for test in medicalTests:
                if test.abbreviation == test_abbreviation:
                    medicalTests.remove(test)
                    print("Test has been deleted.")


        else:
            print("Deletion canceled.")
            return

    else:
        print("That's not a valid test abbreviation")
        return


    medicalSystemShutDown()
    medicalSystemSetUP()

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
        writer.writerow(['Name', 'Abbreviation', 'Range', 'Unit', 'Date'])

        for test in medicalTests:
            writer.writerow([test.test_name, test.abbreviation, test.test_range, test.unit, test.time_to_be_completed])


def changeResultDate(record):
    from datetime import datetime

    if record.status != "Completed":
        return

    first = record.date
    second = record.test.getTimeToBeCompleted()

    first_datetime = datetime.strptime(first, "%Y-%m-%d %H:%M")
    second_parts = second.split("-")
    days = int(second_parts[0])
    hours = int(second_parts[1])
    minutes = int(second_parts[2])

    from datetime import timedelta
    second_datetime = timedelta(days=days, hours=hours, minutes=minutes)
    result = first_datetime + second_datetime
    result_date = result.strftime("%Y-%m-%d %H:%M")
    record.result_date = result_date


def generateSummaryReports(all_tests):
    def get_summary_criteria():
        print("Select criteria for generating the summary report:")
        print("1 - By Test Name")
        print("2 - By Abnormality")
        print("3 - By Status")

        choice = input("Enter your choice (1/2/3): ")
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Defaulting to all criteria.")
            choice = '1'
        return choice

    def filter_tests(tests, criteria, value=None):
        if criteria == '1':
            if value:
                return [test for test in tests if mtClass.getTestName(test) == value]
            return tests
        elif criteria == '2':
            if value is not None:
                return [test for test in tests if validCheck.upNormalResult(test) == value]
            return tests
        elif criteria == '3':
            if value:
                return [test for test in tests if test.getStatus() == value]
            return tests
        return tests

    criteria = get_summary_criteria()

    value = None
    if criteria in ['1', '3']:
        value = input("Enter the value to filter by: ")

    filtered_tests = filter_tests(all_tests, criteria, value)

    if not filtered_tests:
        print("No records found to generate a summary.")
        return

    min_values = {}
    max_values = {}
    total_values = {}
    counts = {}

    min_times = {}
    max_times = {}
    total_times = {}

    abnormal_count = {'Abnormal': 0, 'Normal': 0}
    status_count = {}

    for test in filtered_tests:
        test_name = test.getTestName()
        abnormal = test.isAbnormal()
        status = test.getStatus()

        # Initialize dictionaries for new criteria
        if test_name not in min_values:
            min_values[test_name] = float('inf')
            max_values[test_name] = float('-inf')
            total_values[test_name] = 0
            counts[test_name] = 0

        if test_name not in min_times:
            min_times[test_name] = float('inf')
            max_times[test_name] = float('-inf')
            total_times[test_name] = 0

        test_range = test.getRange()
        test_value = test_range[0] if test_range[0] != 0 else test_range[1]
        min_values[test_name] = min(min_values[test_name], test_value)
        max_values[test_name] = max(max_values[test_name], test_value)
        total_values[test_name] += test_value
        counts[test_name] += 1

        test_time = time_to_minutes(test.getTimeToBeCompleted())
        min_times[test_name] = min(min_times[test_name], test_time)
        max_times[test_name] = max(max_times[test_name], test_time)
        total_times[test_name] += test_time

        # Update abnormality counts
        if abnormal:
            abnormal_count['Abnormal'] += 1
        else:
            abnormal_count['Normal'] += 1

        # Update status counts
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

    # Print results
    print("\nSummary Report:")
    for test_name in min_values:
        average_value = total_values[test_name] / counts[test_name]
        average_time = total_times[test_name] / counts[test_name]

        print(f"\nTest Name: {test_name}")
        print(f"Minimum Test Value: {min_values[test_name]}")
        print(f"Maximum Test Value: {max_values[test_name]}")
        print(f"Average Test Value: {average_value:.2f}")

        print(f"Minimum Turnaround Time: {minutes_to_time(min_times[test_name])}")
        print(f"Maximum Turnaround Time: {minutes_to_time(max_times[test_name])}")
        print(f"Average Turnaround Time: {minutes_to_time(average_time)}")

    print("\nAbnormality Summary:")
    print(f"Abnormal Tests: {abnormal_count['Abnormal']}")
    print(f"Normal Tests: {abnormal_count['Normal']}")

    print("\nStatus Summary:")
    for status, count in status_count.items():
        print(f"Status: {status} - Count: {count}")

def minutes_to_time(minutes):
    days = minutes // (24 * 60)
    hours = (minutes % (24 * 60)) // 60
    minutes = minutes % 60
    return f"{days:02d}-{hours:02d}-{minutes:02d}"
