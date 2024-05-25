#To_Do_List Project
tasks =[]


def addTask():
    task = input("Please enter a task\n")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}.{task}")

            ### Task #1. Take out the groceries
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Please select the no. of the task you want to delete:\n"))
        if taskToDelete>=0 and  taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task{taskToDelete} has been removed")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input")



     

if __name__ == "__main__":
   print("Welcome to the to do list app") 
#create a while loop that runs infinitely until we tell it to stop
while True:
    print("\n")
    print("What would you like to do?\n ")
    print("Please select one of the following options below:")
    print("1. Add a new task")
    print("2.Delete a task")
    print("3.List tasks")
    print("4.Quit")

    user_choice = input("Please select your choice>>>>\n")
    if(user_choice== "1"):
        addTask()
    elif(user_choice=="2"):
        deleteTask() 
    elif(user_choice=="3"):
        listTasks()
    elif(user_choice=="4"):
        break
    else:
        print("Invalid input, Please try again")

print("Goodbye 👋👋👋")


