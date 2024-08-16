import addNewMedicalRecord

class Patient():

    def __init__(self, id):
        self.id = id




def menu():
    print("Welcome to The Clinical System")
    while True:
        print("1- Add new medical record")
        print("2- Add new medical test")
        print("3- update an existing medical record")
        print("4- delete an existing medical record")
        print("5- exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addNewMedicalRecord