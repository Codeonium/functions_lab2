# ### Learning Objectives
# - Learn how to break down code into smaller chunks
# - Learn how to use functions to encapsulate code
# - Refactor the task list program to use functions

# ### Brief

# Given the following list of dictionaries, use functions throughout to create a program to manage a task list.


tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# ### MVP

# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks
def uncomp_task(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["completed"] == False:
            tasks_filtered.append(task["description"])
    return tasks_filtered
tasks_not_completed = uncomp_task(tasks)
print(f"This tasks have not been completed: {tasks_not_completed}")

# 2. Print a list of completed tasks
def comp_task(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["completed"] == True:
            tasks_filtered.append(task["description"])
    return tasks_filtered
tasks_completed = comp_task(tasks)
print(f"The following tasks are the reason you can have your feet up: {tasks_completed}")

# 3. Print a list of all task descriptions
def all_tasks(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["description"]:
            tasks_filtered.append(task["description"])
    return tasks_filtered
all_tasks_result = all_tasks(tasks)
print(f"And here I present to you, all the tasks you had for today: {all_tasks_result}")

# 4. Print a list of tasks where time_taken is at least a given time
def time_it_takes(tasks_list):
    tasks_filtered = []
    for task in tasks_list:
        if task["time_taken"] > 10:
            tasks_filtered.append(task["description"])
    return tasks_filtered
timed_task = time_it_takes(tasks)
print(f"The following tasks all take more than 10 minutes: {timed_task}")

# 5. Print any task with a given description
def task_descript(tasks_list, task_description):
    tasks_filtered = []
    for task in tasks_list:
        if task["description"] == task_description:
            tasks_filtered.append(task["description"])
    return tasks_filtered
tasks_result = task_descript(tasks, "Feed Cat")
print(f"Hey, don't forget: {tasks_result}")

# 6. Given a description update that task to mark it as complete.

# 7. Add a task to the list

# ### Further Extensions

# 8. Use a while loop to display the following menu and allow the use to enter an option.

# ```python
# print("Menu:")
# print("1: Display All Tasks")
# print("2: Display Uncompleted Tasks")
# print("3: Display Completed Tasks")
# print("4: Mark Task as Complete")
# print("5: Get Tasks Which Take Longer Than a Given Time")
# print("6: Find Task by Description")
# print("7: Add a new Task to list")
# print("M or m: Display this menu")
# print("Q or q: Quit")
# ```

# 9. Call the appropriate function depending on the users choice.
