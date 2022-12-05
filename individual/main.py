import functions
import classes

#if the __name__ variable when the program is interpreted equals to __main__, call:
if __name__ == "__main__":
    #reading from the patients file to intialize the patient list
    functions.readPatientsFile(".//data//patients.txt")

    #passing control to the main menu and its sub-menus 
    functions.mainMenu()

    #sorting the patient list
    classes.Patient.sortPatientListByID()

    #writing the new list back to the original file
    functions.writePatientListToFile(".//data//patients.txt")
    