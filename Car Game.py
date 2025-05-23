print ('''
Press (S) to start car!
Press (t) to stop car!
press (q) to exit!
''')
motion=False
while True:
	command = input(" >  ").lower()
	if command ==("s"):
		if not motion:
			print ("Car started... Ready to go!!!")
		else:
			print ("Car is already started!!!")
		motion =True
	elif command == ("t"):
		if motion:
			print ("Car stopped!!!")
		else:
			print ("Car is already stopped!!!")
		motion=False
	elif command ==("q"):
		break
	else:
		print ("Sorry, I didn't understand!")
