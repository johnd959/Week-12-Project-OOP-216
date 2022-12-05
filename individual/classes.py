#patient class
class Patient:
    #initalizing the patient list as a class variable
    patientList = []

    #a class method for sorting the list
    def sortPatientListByID():
        list.sort(Patient.patientList, key=lambda patient: int(patient.getInfo("ID")))
    
    #initialization method for instantiation 
    def __init__(self, ID, Name, Diagnosis, Gender, Age):
        self.__ID = ID
        self.__Name = Name
        self.__Diagnosis = Diagnosis 
        self.__Gender = Gender
        self.__Age = Age
        #appending the new object to the class-wide list
        Patient.patientList.append(self)

    #a method for formatting patient information
    def formatPatientInfo(self):
        info = [self.__ID, self.__Name, self.__Diagnosis,
        self.__Gender, self.__Age]
        #iterating over the info list and building the formatted string
        formattedInfo = "_".join(info)
        return formattedInfo

    #a getter method, a desired case is passed in as an argument
    def getInfo(self, case):
        #matching the case and returning the desired piece of information
        match case:
            case "ID":
                return self.__ID
            case "Name":
                return self.__Name
            case "Diagnosis":
                return self.__Diagnosis
            case "Gender":
                return self.__Gender
            case "Age":
                return self.__Age

    #a setter method, a dictionary with the new information is passed in as an argument
    def changeInfo(self, newinfo):
        #iterating over the dict
        for key, info in newinfo.items():
            #checking if the value of info is empty 
            if info == "":
                #continuing if so
                continue
            #matching the key and setting the object's info with the new values
            match key:
                case "ID":
                    self.__ID = info
                case "Name":
                    self.__Name = info
                case "Diagnosis":
                    self.__Diagnosis = info
                case "Gender":
                    self.__Gender = info
                case "Age":
                    self.__Age = info
                
    #a __str__ method to return a formatted string when an object needs to be printed
    def __str__(self):
        return f"{self.__ID:<10s}{self.__Name:<10s}{self.__Diagnosis:<10s}{self.__Gender:<10s}{self.__Age:<10s}"
