abc="r"
while abc=="r":

    num=[0]*5

    i=0
    while i<=len(num)-1:
        num[i]=int(input("Enter Number "+str(i+1)+"? :: "))
        i=i+1

    searchnum=int(input("Enter Number to search? ::  "))

    first=0
    last=len(num)-1
    mid=int((first+last)/2)

    while first<=last:
        if searchnum==num[mid]:
            print (str(searchnum)+" found at position "+str(mid+1)+".")
            break
        elif searchnum>num[mid]:
            first=mid+1
        else:
            last=mid-1

        mid=int((first+last)/2)

    if first>last:
        print ('''Sorry, Value doesn't exist!
        Invalid Input''')


    print ('''Press (r) to re-run the program.
    Press any key to end the program.''' )
    abc=input().lower()
