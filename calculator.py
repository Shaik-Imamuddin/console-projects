while True:
    print("Select operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice = input("Enter choice(1/2/3/4): ")
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input!")
    else:
        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "+", num2, "=", num1+num2)

        elif choice == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "-", num2, "=", num1-num2)

        elif choice == '3':
             num1 = int(input("Enter first number: "))
             num2 = int(input("Enter second number: "))
             print(num1, "*", num2, "=", num1*num2)

        elif choice == '4':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "/", num2, "=", num1/num2)
    next_calculation = input("Let's do next calculation? (yes/no): ").lower()
    if next_calculation == "no":
        break
    else:
        print("Enter yes or no")
print("Thank You for using my calculator")
