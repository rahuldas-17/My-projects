num=[0]*7

i=0
while i<len(num):
    num[i]=int(input(f"Enter number {i+1}? ::  "))
    i=i+1

j=1
while j<len(num):
    temp=num[j]
    k=j-1
    while temp<num[k] and k>=0:
        num[k+1]=num[k]
        k=k-1
        num[k+1]=temp
    j=j+1

i=0
while i<len(num):
    print (num[i])
    i=i+1
