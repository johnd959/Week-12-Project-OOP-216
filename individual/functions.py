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

#uses getPatientInfo to get input and instantiates a new object with the patient class
def enterPatientInfo():
    info = getPatientInfo()
    newPatient = classes.Patient(info["ID"], info["Name"], info["Diagnosis"], info["Gender"], info["Age"])
    return newPatient

#opens a file from the path passed in as an argument
def readPatientsFile(filePath):
    with open(filePath, "r") as file:
        for line in file:
            #checking if it is the file's legend
            if line.rstrip() == PKEY:
                continue
            else:
                #strips whitespace and pslits the line with at underscores
                items = line.rstrip().split("_")
                #passing in the information obtained into the Patient class
                newPatient = classes.Patient(items[0], items[1], items[2], items[3], items[4])

# iterates over the patient list and checking for a match with the ID argument
def searchPatientByID(Id):
    for patient in classes.Patient.patientList:
        if patient.getInfo("ID") == Id:
            # returning an object if there is a match
            return patient
    # returning -1 if there is none
    return -1 

# searches for a patient with a matching ID and uses the object's setter methods to edit its information
def editPatientInfo(Id):
    #searching for the patient by ID
    searchee = searchPatientByID(Id)
    if searchee == -1:
        print("Patient not in patient file")
        return
    else:
        print(searchee)
    # using the object's setter method to update its information obtained from getPatientInfo in "(e)dit" mode
    searchee.changeInfo(getPatientInfo("e"))
    displayPatientsList()

#iterates over patient list and prints its information using the formatPatientInfo method
def displayPatientsList():
    print(PKEYF)
    for patient in classes.Patient.patientList:
        print(patient)

#opens a file and iterates over the patient list, writing each to the file with the formatPatientInfo method
def writePatientListToFile(filename):
    with open(filename, "w") as file:
        file.write(f"{PKEY}\n")
        for patient in classes.Patient.patientList:
            file.write(f"{patient.formatPatientInfo()}\n")

#leverages capabilities of editPatientInfo to add a patient to the list            
def addPatientToList():
    enterPatientInfo()

# a function to get patient information, default: "(a)dd mode"
def getPatientInfo(mode="a"):
    #initializing a dictionary for patient information 
    patientInfo = {"ID": "", "Name": "", "Diagnosis": "", "Gender": "", "Age": ""}
    #for every key in the dict, get its corresponding info
    for key in patientInfo:
        Valid = False
        #checking for the mode, to skip ID in edit mode
        if mode == "e" and key == "ID":
            continue
        while Valid == False:
            # matching dict key
            match key:
                case "ID":
                    Id = input("Enter Patient ID: ").rstrip()
                    if Id.isdigit() and searchPatientByID(Id) == -1:
                        patientInfo[key] = Id
                    else:
                        print("Enter a nonexisting ID in the proper format")
                        #"continue's" ensure that if the preceding checks are not satisifed, the loop will begin again
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
                        message = "Enter Patient Sex: "
                    elif mode == "e":
                        message = "Enter new Sex: "
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
            # unless the checks are satisfied for the current piece of info, the while loop will never be exited,
            Valid = True
    return patientInfo

#patients menu function
def patientsMenu():
    print(PATMENU)
    option = getOption()
    #while the option is within the acceptable range and not zero, repeat
    while option > 0 and option < 5:
        #matching user sleection to the appropriate functions
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
        #asking for a selection again
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

#main menu function 
def mainMenu():
    print(MAINMENU)
    #asking for a selection 
    option = getOption()
    print("")
    #if the selection is within the valid range and not zero repeat
    while option > 0 and option < 5:
        #matching the user's selection to the appropriate function
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
        #asking for a selection again
        option = getOption()
        print("")

# extra necessary functions

# a function for validating user integer input
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


def getOption(limit=4):
    option = ""
    while option == "" or int(option) > limit:
        option = validateIntInput("Enter option: ", "Please enter a valid option")
    return option