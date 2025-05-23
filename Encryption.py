MyMessage = input("Enter message : ")
EncryptString = ""
for i in range(0, len(MyMessage)) :
	NextNum = ord(MyMessage[i]) + 3
	EncryptString = EncryptString + chr(NextNum)
print(EncryptString)

a=input()
