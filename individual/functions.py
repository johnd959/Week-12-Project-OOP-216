import classes

# Patient-related funtions
PKEY = "ID_Name_Diagnosis_Gender_Age"
PKEYF = f"{'ID':<10s}{'Name':<10s}{'Diagnosis':<10s}{'Gender':<10s}{'Age':<10s}\n"
PATMENU = '''Patient Menu
0 - Return to Main Menu
1 - Display patient's list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info'''
MAINMENU = '''Main Menu
0 - Close application
1 - Doctors
2 - Facilities
3 - Laboratories
4 - Patients'''

def enterPatientInfo():
    info = getPatientInfo()
    newPatient = classes.Patient(info["ID"], info["Name"], info["Diagnosis"], info["Gender"], info["Age"])
    return newPatient

def readPatientsFile(filePath):
    with open(filePath, "r") as file:
        for line in file:
            if line.rstrip() == PKEY:
                continue
            else:
                items = line.rstrip().split("_")
                newPatient = classes.Patient(items[0], items[1], items[2], items[3], items[4])

def searchPatientByID(Id):
    for patient in classes.Patient.patientList:
        if patient.getInfo("ID") == Id:
            return patient
    return -1 

def editPatientInfo(Id):
    searchee = searchPatientByID(Id)
    if searchee == -1:
        print("Patient not in patient file")
        return
    else:
        print(searchee)
    searchee.changeInfo(getPatientInfo("e"))
    displayPatientsList()

def displayPatientsList():
    print(PKEYF)
    for patient in classes.Patient.patientList:
        print(patient)

def writePatientListToFile(filename):
    with open(filename, "w") as file:
        file.write(f"{PKEY}\n")
        for patient in classes.Patient.patientList:
            file.write(f"{patient.formatPatientInfo()}\n")
            
def addPatientToList():
    enterPatientInfo()

def getPatientInfo(mode="a"):
    patientInfo = {"ID": "", "Name": "", "Diagnosis": "", "Gender": "", "Age": ""}
    for key in patientInfo:
        Valid = False
        if mode == "e" and key == "ID":
            continue
        while Valid == False:
            match key:
                case "ID":
                    Id = input("Enter Patient ID: ").rstrip()
                    if Id.isdigit() and searchPatientByID(Id) == -1:
                        patientInfo[key] = Id
                    else:
                        print("Enter a nonexisting ID in the proper format")
                        continue
                case "Name":
                    if mode == "a":
                        message = "Enter Patient Name: "
                    elif mode == "e":
                        message = "Enter new Name: "
                    Name = input(message).rstrip()
                    if Name.isalpha():
                        patientInfo[key] = Name
                    else:
                        print("Enter a valid name")
                        continue
                case "Diagnosis":
                    if mode == "a":
                        message = "Enter Patient Diagnosis: "
                    elif mode == "e":
                        message = "Enter new Diagnosis: "
                    Diagnosis = input(message).rstrip()
                    patientInfo[key] = Diagnosis
                case "Gender":
                    if mode == "a":
                        message = "Enter Patient Gender: "
                    elif mode == "e":
                        message = "Enter new Gender: "
                    Gender = input(message).rstrip()
                    if Gender.capitalize() in ["Male", "Female"]:
                        Gender = Gender.capitalize()
                        patientInfo[key] = Gender
                    else:
                        print("Enter one of the two sexes")
                        continue
                case "Age":
                    if mode == "a":
                        message = "Enter Patient Age: "
                    elif mode == "e":
                        message = "Enter new Age: "
                    Age = input(message).rstrip()
                    if Age.isdigit() and int(Age) > 0:
                        patientInfo[key] = Age
                    else:
                        print("Enter a valid age")
                        continue
            Valid = True
    return patientInfo


def patientsMenu():
    print(PATMENU)
    option = getOption()
    while option > 0 and option < 5:
        match option:
            case 1:
                print("")
                displayPatientsList()
                print("")
            case 2:
                Id = str(validateIntInput("Enter patient ID: ", "Please enter a valid ID"))
                result = searchPatientByID(Id)
                if result == -1:
                    print(f"\nPatient with ID {Id} not in patient file\n")
                else:
                    print(f"\n{result}\n")
            case 3:
                addPatientToList()
                print("")
            case 4:
                Id = str(validateIntInput("Enter patient ID: ", "Please enter a valid ID"))
                editPatientInfo(Id)
                print("")
        print(f"{PATMENU}")
        option = getOption()
# doctor related funtions

def doctorsMenu():
    pass
# facilities related funtions

def facilitiesMenu():
    pass

# laboratories related functions

def laboratoriesMenu():
    pass

# required but miscellaneous funtions

def mainMenu():
    print(MAINMENU)
    option = getOption()
    print("")
    while option > 0 and option < 5:
        match option:
            case 1:
                doctorsMenu()
            case 2:
                facilitiesMenu()
            case 3:
                laboratoriesMenu()
            case 4:
                patientsMenu()
        print("")
        print(f"{MAINMENU}")
        option = getOption()
        print("")

# extra necessary functions
def validateIntInput(messg, errmessg):
    intP = ""
    while intP == "":
        intP = input(messg)
        if intP.isdigit() and int(intP) >= 0:
            intP = int(intP)
        else:
            intP = ""
            print(errmessg)
    return intP

def getOption():
    option = ""
    while option == "" or option > 4:
        option = validateIntInput("Enter option: ", "Please enter a valid option")
    return option