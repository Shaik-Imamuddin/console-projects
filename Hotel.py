import random
while True:
    print("welcome to online hotel booking system")
    name = input("Enter your Name:")
    phno = input("Enter Mobile Number:")
    adhr_no = input("Enter Aadhar Number:")
    print("1.Single Bedroom\n2.Double Bedroom\n3.Triple Bedroom\n4.Quadruple room")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("You Choosen Single Bedroom")
        print("Your room No:", random.randint(200, 500))
        print("Price for 1 day for Single Bedroom = 1000")
        days = int(input("How Many Days You Have to Stay:"))
        print("Total Price = ",(days*1000))
        book = input("Press OK:")
        if book == "OK" or book == "ok":
            print("Booking Successful")
            print("Thanks For Using Online Booking System")
        else:
            print("Enter a Valid input")
    if choice == 2:
        print("You Choosen Double Bedroom")
        print("Your room No:", random.randint(200, 500))
        print("Price for 1 day for Double Bedroom = 2000")
        days = int(input("How Many Days You Have to Stay:"))
        print("Total Price = ",(days*2000))
        book = input("Press OK:")
        if book == "OK" or book == "ok":
            print("Booking Successful")
            print("Thanks For Using Online Booking System")
        else:
            print("Enter a Valid input")
    if choice == 3:
        print("You Cho0sen Triple Bedroom")
        print("Your room No:", random.randint(200, 500))
        print("Price for 1 day for Triple Bedroom = 3000")
        days = int(input("How Many Days You Have to Stay:"))
        print("Total Price = ",(days*3000))
        book = input("Press OK:")
        if book == "OK" or book == "ok":
            print("Booking Successful")
            print("Thanks For Using Online Booking System")
        else:
            print("Enter a Valid input")
    if choice == 4:
        print("You Choosen Quadruple Bedroom")
        print("Your room No:", random.randint(200, 500))
        print("Price for 1 day for Quadruple Bedroom = 3000")
        days = int(input("How Many Days You Have to Stay:"))
        print("Total Price = ",(days*3000))
        book = input("Press OK:")
        if book == "OK" or book == "ok":
            print("Booking Successful")
            print("Thanks For Using Online Booking System")
        else:
            print("Enter a Valid input")
    print("Go for another booking")
    next = input("Enter Yes or No:")
    if next == "no":
        print("Thanks for coming visit again")
        break
else:
    print("Invalid Input")







