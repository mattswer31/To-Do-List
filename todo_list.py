# ANSI escape sequences to print colored text
class bcolors:
    HEADER = '\033[95m'
    COMPLETE = '\033[92m'
    INCOMPLETE = '\033[91m'
    ENDC = '\033[0m'

# Custom exception for when task does not exist
class TaskDoesNotExist(Exception):
    pass

# Custom exception for when an action input is not valid
class ActionIsNotValid(Exception):
    pass

# Adds a task to the list
def add_task(task):
    incomplete_tasks.append(task)

# Displays a formatted list of tasks
def view_tasks():
    print(bcolors.INCOMPLETE + "Incomplete Tasks:")
    for index in range(len(incomplete_tasks)):
        print(f"{index+1}. {incomplete_tasks[index]}")
    print(bcolors.ENDC + bcolors.COMPLETE + "Completed Tasks:")
    for index in range(len(completed_tasks)):
        print(f"{index+1}. {completed_tasks[index]}")
    print(bcolors.ENDC)

# Marks a task as complete or incomplete
def mark_task(task):
    try:
        if task in incomplete_tasks:
            incomplete_tasks.remove(task)
            completed_tasks.append(task)
        elif task in completed_tasks:
            completed_tasks.remove(task)
            incomplete_tasks.append(task)
        else:
            raise TaskDoesNotExist
    except TaskDoesNotExist:
        print(f"{task} is not currently in the list")

# Deletes a task from the list
def delete_task(task):
    try:
        if task in incomplete_tasks:
            incomplete_tasks.remove(task)
        elif task in completed_tasks:
            completed_tasks.remove(task)
        else:
            raise TaskDoesNotExist
    except TaskDoesNotExist:
        print(f"{task} is not currently in the list.")

# Initial Lists of incomplete and completed tasks
completed_tasks = ["go to doctor"]
incomplete_tasks = ["cook dinner", "laundry", "string assignment"]

# Menu message when program initialized
print(bcolors.HEADER +"Welcome to the To-Do List App!"+ bcolors.ENDC)
menu = """
Menu:
1. Add a task
2. View Tasks
3. Mark a task as complete
4. Delete a task
5. Quit\n"""

# Main while loop to control program functions
while True:
    action = input(menu)
    try:
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
            print("Thank for using the To-Do List program!")
            break
        else:
            raise ActionIsNotValid
    except ActionIsNotValid:
        print(f"{action} is not a valid action.")