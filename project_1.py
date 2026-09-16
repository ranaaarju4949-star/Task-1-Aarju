tasks=[]
while True:
    print("\n-----menu-----\n1. Add task\n2. View tasks\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice==2:
        if len(tasks)==0:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice==3:
        print("Exiting the program.")
        break