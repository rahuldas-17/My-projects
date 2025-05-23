class list():
    def __init__(self):
        self.pointer=0
        self.name=""

animallist=[list() for x in range(3)]

def create():
    global animallist
    for n in range(2):
        animallist[n].pointer=n+1

    animallist[2].pointer=-1

    for x in range(3):
        print (animallist[x].pointer)
        print (animallist[x].name)

create()
freepointer=0
headpointer=0

def add(newitem):
    global animallist, currentpointer, previouspointer, headpointer, freepointer, nextfreenode

    if freepointer!=-1:
        animalllist[freepointer].name=newitem
        nextfreenode=animallist[freepointer].pointer
        currentpointer=headpointer
        while animallist [currentpointer].name<=newitem and currentpointer!=-1:
            print ("ran for index"+str(animallist[currentpointer].name))
            previouspointer=currentpointer
            currentpointer=animallist[currentpointer].pointer

        if currentpointer==headpointer:
            animallist[freepointer].pointer=headpointer
            headpointer=freepointer
        else:
            animallist[freepointer].pointer=currentpointer
            animallist[previouspointer].pointer=freepointer
        freepointer=nextfreenode
    else:
        print ("no space")

add(input("value:"))
add(input("value:"))
add(input("value:"))
for x in range(len(animallist)):
    print (str(x)+"----->"+animalist[x].name)
    print (str(x)+"---->"+str(animallist[x].pointer))
print()
print(freepointer)
print(headpointer)

def search():
    global animallist, currentpointer, headpointer, freepointer

    searchitem = input("Item to search? :: ")
    found = False
    currentpointer=headpointer
    while currentpointer!=-1 and found==False:
        if animallist[currentpointer].name==searchitem:
            found=True
            print ("Found!")
        else:
            currentpointer=animallist[currentpointer].pointer
    if found==False:
        print ("Not Found!")

search()
