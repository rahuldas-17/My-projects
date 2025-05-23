nums=[0]*5
top=-1

def push():
    global nums
    global top

    if top==len(nums)-1:
        print ("Stack is full!")
    else:
        n=int(input("Enter Number? :: "))
        top=top+1
        nums[top]=n
        print ("Number added to stack successfully!")

def pop():
    global nums
    global top

    if top==-1:
        print ("Stack is empty!")
    else:
        value=nums[top]
        nums[top]=""
        top=top-1
        print (f"Value {value} removed/deleted from stack successfully!")


pop()
pop()
push()
push()
push()
push()
push()
pop()
pop()
print (nums)
