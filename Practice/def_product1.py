from def_product import *

title=["id","name","address","department"]
student_list = []
op1="yes"
while op1=="yes":
    #data=getInput(title)
    student_list.append(getInput(title))
    op1=input("Do you want to continue?(yes/no)")

for student in student_list:
    display(title,student)
