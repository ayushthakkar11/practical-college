class employee:
    id=0;
    name=""
    department=""
    address=""
    salary=0;

employee_detail=[]
n="yes"

while n!="no":
    e1=employee()
    e1.id=int(input("Enter id="))
    e1.name=input("Enter name=")
    e1.department=input("Enter your department=")
    e1.address=input("Enter address=")
    e1.salary=int(input("Enter salary="))
    employee_detail.append(e1)
    n=input("Do you want to continue?(yes/no)")

for e1 in employee_detail:
    print("id=",e1.id)
    print("Name=",e1.name)
    print("Department=",e1.department)
    print("address=",e1.address)
    print("salary=",e1.salary)