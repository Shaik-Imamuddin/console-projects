print("Welcome to Bank")
a=int(input("Enter Account number:"))
total=1000
for i in range(1,11):
    if i==a:
        print("User Exist")
while True:
    print("1.DEPOSIT\n2.WITHDRAW\n3.BALANCE ENQUIRY\n0.EXIT")
    b=int(input("Enter your choice:"))
    if(b==1):
        dep=int(input("Enter amount to deposit:"))
        total=total+dep
        print("Now your account balance is:",total)
    elif(b==2):
        wth=int(input("Enter amount to withdraw:"))
        total=total-wth
        print("Now your account balance is:",total)
    elif(b==3):
        print("your account balance is:",total)
    elif(b==0):
        print("Thanks for coming visit again")
    else:
        print("Invalid Input")
        break
    next=input("Enter Yes or No:")
    if(next=="no"):
        print("Thanks for coming visit again")
        break
else:
    print("Invalid Input")
        
        
        
