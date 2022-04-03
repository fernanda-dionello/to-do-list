from List import List
from Task import Task

def toDoListProgram():
    toDoList = List()
    done = List()

    while True:
        try:
            choice = int(input(
            '''
            =============================================
            MENU
            =============================================
            1 -	List activities
            2 -	Add Task
            3 -	Delete task
            4 -	Update task
            5 -	Mark a task as completed
            6 -	List completed tasks
            7 -	Finish the application
            =============================================

            Choose one of the options: '''))

            if choice == 1:
                if(toDoList.size != 0):
                    toDoList.getList('')
                else:
                    print("\nThe list is empty.")
            elif choice == 2:
                text = input('\nWrite your task here: ')
                task = Task(text)
                toDoList.addTask(task)
            elif choice == 3:
                if(toDoList.size != 0):
                    toDoList.getList('')
                    task = input('\nSelect the task number you want to delete: ')
                    toDoList.deleteTask(task)
                else:
                    print("\nThe list is empty.")
            elif choice == 4:
                if(toDoList.size != 0):
                    toDoList.getList('')
                    task = input('\nSelect the task number you want to update: ')
                    if task < 0 or task > toDoList.size:
                        print ("This position doesn't exist.")
                    else:
                        newText = input('\nWrite the new text here: ')
                        toDoList.updateTask(task, newText)
                else:
                    print("\nThe list is empty.")
            elif choice == 5:
                if(toDoList.size != 0):
                    toDoList.getList('')
                    task = input('\nSelect the task number you want to mark as done: ')
                    text = toDoList.getTask(task)
                    if(text):
                        newTask = Task(text)
                        done.addTask(newTask)
                        toDoList.deleteTask(task)
                else:
                    print("\nThe list is empty.")
            elif choice == 6:
                if(toDoList.size != 0):
                    done.getList('- DONE')
                else:
                    print("\nThe list is empty.")
            elif choice == 7:
                break
            else:
                print('\nEnter a valid numeric choice: 1, 2 or 3. Try again!')
        except:
            print('\nEnter a valid numeric choice.')

toDoListProgram()
