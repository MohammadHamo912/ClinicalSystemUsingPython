import package as fn

def menu():
    print("Welcome to The Clinical System")
    while True:
        print("1- Add new medical record")
        print("2- Add new medical test")
        print("3- update an existing patient medical record")
        print("4- update an existing medical test")
        print("5- display patient medical record")
        print("6- display patient medical test")
        print("7- delete an existing medical record")
        print("8- delete an existing medical test")
        print("9- generate textual summary report")
        print("10 - export medical records to a csv file")
        print("11 - import medical records from a csv file")
        print("0- exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            fn.addNewMedicalRecords()
        elif choice == 2:
            fn.addNewMeidcalTest()
        elif choice == 3:
            fn.updateMedicalRecords()
        elif choice == 4:
            fn.updateMeidcalTest()
        elif choice == 5:
            fn.displayMedicalRecords()
        elif choice == 6:
            fn.displayMeidcalTest()
        elif choice == 7:
            fn.deleteMedicalRecord()
        elif choice == 8:
            fn.deleteMeidcalTest()
        elif choice == 9:
            fn.generateTextualSummary()
        elif choice == 10:
            fn.exportMedicalRecords()
        elif choice == 11:
            fn.importMedicalRecords()
        elif choice == 0:
            break






menu()