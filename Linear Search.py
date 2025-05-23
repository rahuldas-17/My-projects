names=[""]*5
found=False

i=0
while i<len(names):
	names[i]=input(f"Enter name {i+1} >> ")
	i=i+1

searchname=input("Enter name to search? >> ")

k=0
while k<len(names):
	if names[k]==searchname:
		position=k+1
		found=True
		break
	k=k+1

if found==True:
	print (f"{searchname} found at position {position}!")
else:
	print ("Sorry, Result doesn't exist!")