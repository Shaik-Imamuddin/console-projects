print("Welcome to Bank")
account_number = int(input("Enter Account number: "))
total = 1000
if 1 <= account_number <= 10:
    print("User Exists")
    while True:
        print("\n1. DEPOSIT\n2. WITHDRAW\n3. BALANCE ENQUIRY\n0. EXIT")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            deposit = int(input("Enter amount to deposit: "))
            total += deposit
            print("Amount deposited successfully!")
            print("Now your account balance is:", total)
        elif choice == 2:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw > total:
                print("Insufficient balance!")
            else:
                total -= withdraw
                print("Amount withdrawn successfully!")
                print("Now your account balance is:", total)
        elif choice == 3:
            print("Your account balance is:", total)
        elif choice == 0:
            print("Thanks for coming. Visit again!")
            break
        else:
            print("Invalid Input. Please try again.")
        next_action = input("Do you want to perform another transaction? (yes/no): ").strip().lower()
        if next_action == "no":
            print("Thanks for coming. Visit again!")
            break
else:
    print("Invalid Account Number")
