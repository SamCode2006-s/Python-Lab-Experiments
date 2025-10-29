an="Sam"
ap=2006
bal=100
hist=[]
print("Welcome to SamBank!!!\nPlease login first:")
bn=input("Enter account name: ")
bp=int(input("Enter account pin: "))
if(bn==an and bp==ap):
    while True:
        print("\nWelcome",bn, "to SamBank!\nHow can we help you today?\n1: Deposit\n2: Withdraw\n3: Check Balance\n4: History\n5: Exit\n")
        c=int(input("Enter your choice: "))
        if(c==1):
            d=int(input("Enter amount to deposit: "))
            print("Are you sure to deposit",d,"in you bank account?(Y/N)")
            confirm=input().strip().upper()
            if(confirm=="Y"):
                    bal=bal+d
                    print("Successful!\nNew bank balance:",bal)
                    hist.append(f"DEPOSIT: +{d}")
            else:
                    print("Cancelled")
        elif(c==2):
            w=int(input("Enter amount to withdraw: "))
            if(w>bal):
                print("Insufficient funds!")
            else:
                print("Are you sure to withdraw",w,"in you bank account?(Y/N)")
                confirm=input().strip().upper()
                if(confirm=="Y"):
                    bal=bal-w
                    print("Successful!\nNew bank balance:",bal)
                    hist.append(f"Withdraw: -{w}")
                else:
                    print("Cancelled")
        elif(c==3):
            print("Bank balance: ",bal)
        elif(c==4):
            for i in range(len(hist)):
                print(hist[i])
        elif(c==5):
            print("Thank you for choosing us!")
            break
else:
    print("Wrong input entered!")
    
            

                 
    
