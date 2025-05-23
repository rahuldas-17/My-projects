open=True
while open==True:
    answer=False
    import random
    r=[0,1,2,3,4,5,6,7,8,9]
    b=random.choice(r)
    count=True
    i=0
    while i<=2:
        n=int(input("Guess the number? (0 to 9)  :::   "))
        if n== b:
            answer=True
            break
        if i==2:
            count = False
        if  count==True:
            print ("Try Again!")
        i+=1
    if answer==True:
        print ("CONGRATULATIONS, YOU WON!!!")
    else:
        print ("SORRY, YOU LOST!!!")
    print ('''
The number was ''',b,".")
    a=input('''

    Press any key to re-play!

    ''')
