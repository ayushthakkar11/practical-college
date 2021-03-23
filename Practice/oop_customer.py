class customer:
    id=0
    name=""
    address=""

    def entry(self):
        self.id=input("Enter id=")
        self.name=input("Enter name=")
        self.address=input("Enter address=")

    def view(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("Address=",self.address)

customer_list=[]
op="yes"
while op.lower()=="yes":
    c1=customer()
    c1.entry()
    customer_list.append(c1)
    op=input("Do you want to continue?(yes/no)")

for c1 in customer_list:
    c1.view()