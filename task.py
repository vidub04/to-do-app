##To-Do list
##Menu:


def menu():
    print("Menu of Options:")
    print("1. Show Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")
    print("4.Exit")

    n=int(input("Enter Option"))
    if n==1:
        show_task()
    elif n==2:
        add_task()
    elif n==3:
        del_task()
    elif n==4:
        exit()
    else:
        print("Invalid Output")
        menu()
    

def show_task():
    s=len(tasks)
    if s==0:
        print("List Empty!!")
        print()
        print()
    else:
        for i in range(0,s):
            print(i+1,".",tasks[i])

    menu()

def add_task():
    s=input("Enter Task Description")
    tasks.append(s)
    print("Task Entered Successfully")
    print()
    print()
    menu()

def del_task():
    s=len(tasks)
    if s==0:
        print("No Tasks")
        print()
        print()
    else:
        for i in range(0,s):
            print(i+1,".",tasks[i])

        t=int(input("Enter task to delete:"))
        tasks.pop(t-1)
        print("Deleted Task")

        print()
        print()

    
    menu()

def exit():
    print("ThankYou")


tasks=[]

menu()

    



