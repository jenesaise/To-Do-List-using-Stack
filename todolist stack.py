TaskList = [""]*10
tos = -1 

def AddTask():
    global TaskList, tos
    
    Task = input("Enter A Task To Do = ")
    if tos == 9:
        print("Your Tasks List Is Full...")
    else:
        tos = tos + 1
        TaskList[tos] = Task
        print("Task Added!")

def DisplayTask():
    global TaskList, tos

    print("Your Tasks To Do Are =", TaskList)
    print("The Value Of The Top Of Stack Is = ", tos)

def RemovedTask():
    global TaskList, tos
    if tos == -1:
        print("Your Tasks List Is Empty...")
    else:
        TaskList[tos] = ""
        tos = tos - 1
        print("Task Removed!")

def Main():
    global TaskList, tos
    choice = 0 
    while choice != 4:
        print("1 = Add A Task")
        print("2 = View Task")
        print("3 = Remove Task")
        print("4 = Exit")

        choice = int(input("Enter Your Choice = "))
        if choice == 1:
            AddTask()
        elif choice == 2:
            DisplayTask()
        elif choice == 3:
            RemovedTask()
        elif choice == 4:
            print("Thank You For Using The To Do List!")
            break
        else:
            ("Invalid Choice Enterred...")
            choice = int(input("Re-enter Your Choice = "))
    
Main()