a=("")
while a!="exit":

	def oddeven(num):
		if num%2==0:
			message=(str(n)+" is even number!")
		else:
			message=(str(n)+" is odd number!")
		return message

	n=int(input("Enter the number? ::  "))
	result=oddeven(n)
	print (result)

	print ('''
Press (Enter) to re-start!
Enter (exit) to exit!
''')
	a=input(">>  ")
