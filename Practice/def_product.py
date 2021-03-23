def getInput(title):
    values=[]
    for t in title[0:]:
        values.append(input("enter "+t+"="))

    return values

def display(title,values):
    for t,v in zip(title,values):
        print(t,v)
