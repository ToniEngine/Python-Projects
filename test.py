tasks =[]


def addTask():
    task = input("Please enter a task\n")
    tasks.append(task)
    print(f"Task: '{task}' has been added to the list.")

addTask()
print(tasks)