class info:
    name=""
    address=""
    phno=""

    def setinfo(self):
        self.name=input("Enter name=")
        self.address=input("Enter address=")
        self.phno=input("Enter address=")

    def getinfo(self):
        print("Nmae=",self.name)
        print("Address=",self.address)
        print("Phone Number=",self.phno)

class department(info):
    id=""
    department=""
    