class product:
    name=""
    id=0
    rates=0
    quantity=0

class customer:
    name=""    
    address=""
    contact=0
    bill_no=0
    product_list=""
    
bill_detail=[]
p=product()
n="yes"
n2="yes"


while n2!="no":
    c = customer()
    c.bill_no = int(input("Enter customer id="))
    c.name = input("enter customer name=")
    c.contact = int(input("Enter contact number="))
    c.address = input("Enter address=")
    c.product_list = []
    n="yes"
    while n!="no":
        p=product()
        p.id = int(input("enter product id="))
        p.name = input("enter product name=")
        p.rates = int(input("enter product rates="))
        p.quantity = int(input("enter product quantity="))
        c.product_list.append(p)
        n=input("Do you want to continue entering product details?(yes/no)")

    bill_detail.append(c);
    n2 = input("Do you want to continue entering bill details?(yes/no)")


for c in bill_detail:
    print("Bill no=",end="")
    print(c.bill_no)
    print("c_name=",end="")
    print(c.name)
    print("contact=",end="")
    print(c.contact)
    print("Address=")
    print(c.address)
    total=0
    print("Pid \t pname \t prates \t pquntity ")
    for p in c.product_list:
        print(p.id,"\t\t",p.name,"\t", p.rates,"\t", p.quantity)
        price=p.rates*p.quantity
        total=total+price

    print("Total :",total)
    print("==================================================")


