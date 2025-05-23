names=[""]*5
front=-1
rear=-1

def addtoqueue():
    global names
    global front
    global rear

    if (front==rear+1) or ((front==0) and rear==len(names)-1):
        print ("Queue is full!")
    else:
        if (front==-1):
            front=0
        getname=input("Enter name? :: ")
        rear=(rear+1)%len(names)
        names[rear]=getname
        print (f"{getname} is added to queue successfully!")

def deletefromqueue():
    global names
    global front
    global rear

    if (front==-1):
        print ("Queue is Empty!")
    else:
        value=names[front]
        names[front]=""
        if (front==rear):
            front=-1
            rear=-1
        else:
            front=(front+1)%len(names)
        print (f"{value} deleted successfully from queue!")

addtoqueue()
addtoqueue()
addtoqueue()
print (names)
deletefromqueue()
deletefromqueue()
print (names)
addtoqueue()
addtoqueue()
addtoqueue()
addtoqueue()
print (names)
addtoqueue()
