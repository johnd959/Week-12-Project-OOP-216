class Patient:
    patientList = []
    def sortPatientListByID():
        list.sort(Patient.patientList, key=lambda patient: int(patient.getInfo("ID")))
    
    def __init__(self, ID, Name, Diagnosis, Gender, Age):
        self.__ID = ID
        self.__Name = Name
        self.__Diagnosis = Diagnosis 
        self.__Gender = Gender
        self.__Age = Age
        Patient.patientList.append(self)

    def formatPatientInfo(self):
        info = [self.__ID, self.__Name, self.__Diagnosis,
        self.__Gender, self.__Age]
        formattedInfo = "_".join(info)
        return formattedInfo

    def getInfo(self, case):
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

    def changeInfo(self, newinfo):
        for key, info in newinfo.items():
            if info == "":
                continue
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

    def __str__(self):
        return f"{self.__ID:<10s}{self.__Name:<10s}{self.__Diagnosis:<10s}{self.__Gender:<10s}{self.__Age:<10s}"
