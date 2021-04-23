import  psycopg2
#make connection
conn=psycopg2.connect(host="localhost",
                      dbname="pythonDB",
                      user="postgres",
                      password="Merci@@11")
cur=conn.cursor()
op1=1
while op1!=3:
    print("\t Student Info")
    print(" press 1 for Entry")
    print(" press 2 for View")
    print(" press 3 for Search ")
    print(" press 4 for Update ")
    print(" press 5 for exit")

    op1=int(input("Enter your option :"))

    if op1 == 1:
        op2="yes"
        while op2.lower()=="yes":
            rno=int(input("Enter Roll No:"))
            name=input("Enter Name :")
            maths=int(input("Enter Maths marks:"))
            sci=int(input("Enter Sci marks:"))
            eng=int(input("Enter Eng marks:"))

            cur.execute("insert into student_info values (%s,%s,%s,%s,%s)", (rno, name, maths, sci, eng))
            conn.commit()
            op2=input("do you want to add another student(yes/no)?:")

    elif op1 == 2:
         print("\t view ")
         #print("RollNo\tName\tMath\tScience\tEnglish")
         cur.execute("select rollno,sname,maths,sci,eng, maths+sci+eng ,case (maths>35 and sci>35 and eng>35 ) when true then 'pass' else 'fail' end   from student_info order by maths desc")
         for row in cur:
             for value in row:
                print(value,end="\t")
             print("")

    elif op1==3:
        print("\t\t search ")
        srno=int(input("Enter Roll No:"))
        #print("RollNo\tName\tMath\tScience\tEnglish")
        cur.execute("select rollno,sname,maths,sci,eng, maths+sci+eng ,case (maths>35 and sci>35 and eng>35 ) when true then 'pass' else 'fail' end   from student_info where rollno=%s",(srno,))
        for row in cur:
            for value in row:
                print(value, end="\t")
            print("")
    elif op1==4:
        print("\t\t update")
        srno=int(input("Enter Roll no:"))
        print("1.name")
        print("2.marks")
        print("3.exit")
        op3=int(input("Enter"))
        while op3!=3:
            if op3==1:
                sname=input("Enter name")
                cur.execute("update student_info set sname=%s where rollno=%s",(sname,srno))
            elif op3==2:
                print("1.Maths")
                print("2.Science")
                print("3.English")
                print("4.Exit")
                op4=1
                while op4!=4:
                    if op4==1:
                        maths=int(input("Enter marks="))
                        cur.execute("update student_info set maths=%s where rollno=%s",(maths,srno))
                    elif op4==2:
                        sci=int(input("Enter marks="))
                        cur.execute("update student_info set sci=%s where rollno=%s",(sci,srno))
                    elif op4==3:
                        eng=int(input("Enter marks="))
                        cur.execute("update student_info set eng=%s where rollno=%s",(eng,srno))

                    elif op4==4:
                        exit()
                    else:
                        print("Enter valid input")
            elif op3==3:
                exit()
    elif op2==5:
        exit()
    else :
        print("wrong option selected try again ")

cur.close()
conn.close()