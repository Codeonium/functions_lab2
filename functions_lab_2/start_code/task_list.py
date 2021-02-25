tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:
task_input = ""
time_task = ""
task_desc = ""
# 1. Print a list of uncompleted tasks
def uncomp_task(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["completed"] == False:
            tasks_filtered.append(task["description"])
    return tasks_filtered
tasks_not_completed = uncomp_task(tasks)
#print(f"This tasks have not been completed: {tasks_not_completed}")

# 2. Print a list of completed tasks
def comp_task(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["completed"] == True:
            tasks_filtered.append(task["description"])
    return tasks_filtered
tasks_completed = comp_task(tasks)
#print(f"The following tasks are the reason you can have your feet up: {tasks_completed}")

# 3. Print a list of all task descriptions
def all_tasks(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["description"]:
            tasks_filtered.append(task["description"])
    return tasks_filtered
all_tasks_result = all_tasks(tasks)
#print(f"And here I present to you, all the tasks you had for today: {all_tasks_result}")

# 4. Print a list of tasks where time_taken is at least a given time
def time_it_takes(tasks_list, time_task):
    tasks_filtered = []
    for task in tasks_list:
        if task["time_taken"] > 10:
            tasks_filtered.append(task["description"])
    return tasks_filtered
timed_task = time_it_takes(tasks, time_task)
#print(f"The following tasks all take more than 10 minutes: {timed_task}")

# 5. Print any task with a given description
def task_descript(tasks_list, task_description):
    tasks_filtered = []
    for task in tasks_list:
        if task["description"] == task_description:
            tasks_filtered.append(task["description"])
    return tasks_filtered
tasks_result = task_descript(tasks, task_desc)
#print(f"Hey, don't forget: {tasks_result}")

# 6. Given a description update that task to mark it as complete.
def task_now_completed(tasks_list, task_description):
    tasks_filtered = []
    for task in tasks_list:
        if task["completed"] == False:
            task["completed"] = True
            return tasks_filtered
tasks_now_result = task_now_completed(tasks, task_input)
print(tasks_now_result)

# 7. Add a task to the list
tasks.append({"description": "Relax",
        "completed": False, 
        "time_taken": 1 
})
#print(tasks)
# ### Further Extensions

# 8. Use a while loop to display the following menu and allow the use to enter an option.
#while True:

print("Menu:")
print("1: Display All Tasks")
print("2: Display Uncompleted Tasks")
print("3: Display Completed Tasks")
print("4: Mark Task as Complete")
print("5: Get Tasks Which Take Longer Than a Given Time")
print("6: Find Task by Description")
print("7: Add a new Task to list")
print("M or m: Display this menu")
print("Q or q: Quit")
#User = input("Please input your command for access ")
while True:
    User = int(input("Please input your command for access "))
    if User == 1:
        print(f"And here I present to you, all the tasks you had for today: {all_tasks_result}")
    elif User == 2:
        print(f"This tasks have not been completed: {tasks_not_completed}")
    elif User == 3:
        print(f"The following tasks are the reason you can have your feet up: {tasks_completed}")
    elif User == 4:
        task_input = input("Please enter the name of the task you want to mark as completed? ")
        tasks_now_result = task_now_completed(tasks, task_input)
        print(tasks_now_result)
    elif User == 5:
        time_task = input("Enter the minimum time you want the task to have ")
        timed_task = time_it_takes(tasks, time_task)
        print(f"The following tasks all take more than 10 minutes: {timed_task}")
    elif User == 6:
        task_desc = input ("Please enter the description of the task you are looking for ")
        tasks_result = task_descript(tasks, task_desc)
        print(f"Hey, don't forget: {tasks_result}")
    elif User == 7:
        tasks.append({"description": "Relax",
            "completed": False, 
            "time_taken": 1 
        })
        print(tasks)
    elif User == "M" or "m":
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")
        User = int(input("Please input your command for access "))
    else:
        print("bye bye!")
        break


# 9. Call the appropriate function depending on the users choice.
