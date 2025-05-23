num=[0]*5

k=0
while k<len(num):
    num[k]=int(input(f"Enter Number {k+1}? ::  "))
    k=k+1

p=0
while p<len(num)-1:
    i=0
    while i<(len(num)-1)-p:
        if num[i]>num[i+1]:
            temp=num[i]
            num[i]=num[i+1]
            num[i+1]=temp
        i=i+1
    p=p+1

j=0
while j<len(num):
    print (int(num[j]))
    j=j+1
