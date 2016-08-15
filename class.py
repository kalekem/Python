class Person:
    def __init__(self, idN): # constructor
        self.idN = idN
        print("Our class is created")

    def __del__(self):
        print (self.idN, "Our class object is destroyed") # destructor  
        
    def setFullName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        print(self.firstName, " ", self.lastName)

personName = Person(7)
personName.setFullName("Cleophas", "Kalekem")
personName.printFullName()
personName.__del__()
    
