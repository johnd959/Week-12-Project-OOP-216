import functions
import classes

if __name__ == "__main__":
    functions.readPatientsFile(".//data//patients.txt")
    functions.mainMenu()
    classes.Patient.sortPatientListByID()
    functions.writePatientListToFile(".//data//patients.txt")
    