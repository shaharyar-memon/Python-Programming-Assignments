# To-do Application

# Application will run in a loop, will always show the list and menu, and will contain :
# displayTask() function
# mainMenu() function
# addTask() function
# removeTask() function
# removeAllTasks() function
# exitApp() function

tasks = []
menu = ['Add Task', 'Remove Task', 'Remove all tasks', 'Exit']

def displayTask():
    for i in tasks:
        print(tasks.index(i)+1, '. ', i)

def mainMenu():
    print('\n--- Main Menu ---')
    for j in menu:
        print(menu.index(j)+1, '. ', j)

    option = 0
    while(True):
        try:
            option = int(input("Enter the number associated with the option you want to access:"))
            break
        except ValueError:
            print('Invalid entry. Try again.')
    return option

def addTask():
    task = input('\nEnter task:')
    tasks.append(task)
    print('Task added!\n')

def removeTask():
    while(True):
        try:
            task = input('\nEnter task to remove:')
            tasks.remove(task)
            break
        except ValueError:
            print('Invalid entry. Please try again.')
    print('Task removed.\n')

def removeAllTasks():
    tasks.clear()
    print('All tasks removed.\n')

print('--- TODO APPLICATION ---')

while(True):
    displayTask()
    option = mainMenu()

    if option == 1:
        addTask()
    elif option == 2:
        removeTask()
    elif option == 3:
        removeAllTasks()
    else:
        print('Exiting...')
        break