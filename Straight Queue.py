names = [""]*5
front = -1
rear =-1

def addtoqueue():
    global names
    global front
    global rear

    if rear == len(names)-1:
        print ("Queue is full!")
    else:
        if front == -1:
            front = 0
        getname = input("Enter the name? ::  ")
        rear+=1
        names[rear]=getname
        print (f"{getname} added to queue successfully!")

def deletefromqueue():
    global names
    global front
    global rear

    if front == -1:
        print ("Queue is empty!")
    else:
        value = names[front]
        names[front] = ""
        if front == rear:
            front = -1
            rear = -1
        else:
            front += 1
        print (f"{value} removed from queue successfully!")



addtoqueue()
addtoqueue()
addtoqueue()
deletefromqueue()
deletefromqueue()
addtoqueue()
print (names)
