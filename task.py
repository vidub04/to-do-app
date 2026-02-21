##To-Do list
##Menu:

tasks=[]

def menu():
    print("Menu of Options:")
    print("1. Show Tasks")
    print("2. Add Tasks")
    print("3. Delete Tasks")

    n=int(input("Enter Option"))

def show_task():
    s=tasks.len()
    if s==0:
        print("List Empty!!")
    else:
        for i in range(0,s):
            print(i+1,".",tasks[i])

def add_task():
    s=input("Enter Task Description")
    tasks.append(s)

def del_task():
    s=tasks.len()
    if s==0:
        print("No Tasks")
    else:
        for i in range(0,s):
            print(i+1,".",tasks[i])

        t=int(input("Enter task to delete:"))
        tasks.pop(t-1)

    



