tasks = []
while True:
    print("Menu:")
    print("1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    elif choice == '2':
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed successfully!")
        else:
            print(f"Task '{task}' not found!")
    elif choice == '3':
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found!")
    elif choice == '4':
        print("Thank's for using my TO-DO list")
        break
    else:
        print("Invalid choice! Please try again.")
