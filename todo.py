completed_tasks = ["go to doctor"]
incomplete_tasks = ["cooking dinner", "laundry", "to-do list program", "string assignment"]

# Adds a task to the list
def add_task(task):
    incomplete_tasks.append(task)

# Displays a formatted list of tasks
def view_tasks():
    print("Incomplete Tasks:")
    for index in range(len(incomplete_tasks)):
        print(f"{index+1}. {incomplete_tasks[index]}")
    print("Completed Tasks:")
    for index in range(len(completed_tasks)):
        print(f"{index+1}. {completed_tasks[index]}")

# Marks a task as complete or incomplete
def mark_task(task):
    if task in incomplete_tasks:
        incomplete_tasks.remove(task)
        completed_tasks.append(task)

# Deletes a task from the list
def delete_task(task):
    pass

print("Welcome to the To-Do List App!")
while True:
    action = input("""
Menu:
1. Add a task
2. View Tasks
3. Mark a task as complete
4. Delete a task
5. Quit\n""")

    if action == '1':
        task = input("What is the name of the task?")
        add_task(task)
    elif action == '2':
        view_tasks()
    elif action == '3':
        task = input("What is the name of the task you completed?")
        mark_task(task)
    elif action == '4':
        task = input("What is the name of the task you want to delete?")
        delete_task(task)
    elif action == '5':
        print("Thank for using the to-do list!")
        break
    else:
        print("That is not a valid option.")
