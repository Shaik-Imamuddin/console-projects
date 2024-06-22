# Initialize an empty dictionary to store contacts
contacts = {}

# Main loop for the contact list
while True:
# Display the menu
    print("""
    Contact List Mini Project
    -------------------------
    1. Add Contact
    2. View Contacts
    3. Search Contact
    4. Delete Contact
    5. Exit
    """)

    # Take input for choice
    choice = input("Enter your choice: ")

    # Add contact
    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print("Contact added successfully!\n")

    # View contacts
    elif choice == '2':
        if contacts:
            print("Contacts:")
            for name, number in contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts available!\n")

    # Search contact
    elif choice == '3':
        search_name = input("Enter contact name to search: ")
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print("Contact not found!\n")

    # Delete contact
    elif choice == '4':
        delete_name = input("Enter contact name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully!\n")
        else:
            print("Contact not found!\n")

    # Exit the program
    elif choice == '5':
        print("Thank you for using my Contact App!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.\n")

    # Ask user if they want to continue
    next_iteration = input("Do you want to continue (yes/no)? ").lower()
    if next_iteration != 'yes':
        print("Thank you for using my Contact App")
        break
