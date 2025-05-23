data=[""]*5
left=[""]*5
right=[""]*5

def binarytreeinitialisation():
    global data, left, right, free, root

    i=0
    while i<=4:
        data[i]=""
        left[i]="null"
        right[i]="null"
        i=i+1
    free=0
    root=-1


def inserttobinarytree(newitem):
    global data, left, right, free, root
    global current, previous

    leftcheck=False
    rightcheck=False
    current=""
    previous=""

    data[free]=newitem

    if root==-1:
        root=free
        print (f"{newitem} added to binary tree successfully!")
    else:
        current=root

        while current!="null":
            previous=current
            if newitem < data[current]:
                current=left[current]
                if current=="null":
                    leftcheck=True
            else:
                current=right[current]
                if current=="null":
                    rightcheck=True


    if leftcheck==True:
        left[previous]=free
        print (f"{newitem} added to binary tree successfully!")
    if rightcheck==True:
        right[previous]=free
        print (f"{newitem} added to binary tree successfully!")

    index=0
    while index<=4:
        if data[index]=="":
            free=index
            break
        else:
            free=0
        index=index+1

    leftcheck=False
    rightcheck=False

binarytreeinitialisation()
inserttobinarytree("Alok")
inserttobinarytree("Apar")
inserttobinarytree("Nirdesh")
inserttobinarytree("Nisith")
inserttobinarytree("Hari")

print(data)
print(left)
print(right)



