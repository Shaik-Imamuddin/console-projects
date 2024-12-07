import random

print("Welcome to the Online Bus Booking System!")

# Prices for seats
sleeper_price = 500
non_sleeper_price = 300

# Initialize seat counts
sleeper_seats = random.randint(5, 15)#sleeper seats generate randomly 
non_sleeper_seats = random.randint(10, 20)#non-sleeper seats generate randomly 

print(f"Available Sleeper Seats: {sleeper_seats}")
print(f"Available Non-Sleeper Seats: {non_sleeper_seats}")
print(f"Prices - Sleeper: ${sleeper_price}\nNon-Sleeper: ${non_sleeper_price}\n")

# Main booking system loop
while True:
    print("1. Book Sleeper Seat")
    print("2. Book Non-Sleeper Seat")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        if sleeper_seats > 0:
            print(f"Booking a Sleeper Seat (${sleeper_price})")
            confirm = input("Click OK to confirm or Cancel to cancel the booking (OK/Cancel): ").strip().lower()

            if confirm == "ok":
                sleeper_seats -= 1
                print("Sleeper Seat booked successfully!")
            elif confirm == "cancel":
                print("Booking cancelled.")
            else:
                print("Invalid input. Booking cancelled.")
        else:
            print("No Sleeper Seats available!")

    elif choice == "2":
        if non_sleeper_seats > 0:
            print(f"Booking a Non-Sleeper Seat (${non_sleeper_price})")
            confirm = input("Click OK to confirm or Cancel to cancel the booking (OK/Cancel): ").strip().lower()

            if confirm == "ok":
                non_sleeper_seats -= 1
                print("Non-Sleeper Seat booked successfully!")
            elif confirm == "cancel":
                print("Booking cancelled.")
            else:
                print("Invalid input. Booking cancelled.")
        else:
            print("No Non-Sleeper Seats available!")

    elif choice == "3":
        print("Thank you for using Online Bus Booking System!")
        break

    else:
        print("Invalid choice. Please try again.")

    # Display updated seat availability
    print(f"\nUpdated Availability - Sleeper Seats: {sleeper_seats}, Non-Sleeper Seats: {non_sleeper_seats}\n")

    #get user input to go for another booking
    another_booking = input("Would you like to make another booking? (yes/no): ").strip().lower()
    if another_booking != "yes":
        print("Thank you for using Online Bus Booking System!")
        break
