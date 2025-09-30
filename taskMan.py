# Show tasks on To-Do list
def show_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return
    print("\nYour tasks:")
    for idx, (title, priority) in enumerate(tasks, start=1):
        print(f"{idx}. {title} (priority {priority})")
    print()
# Add task to list
def add_tasks(tasks):
    title = input("Task title: ").strip()
    while True:
        try:
            priority = int(input("Priority (1=high, 5=low):").strip())
            if 1 <= priority <= 5:
                break
            print("Priority must be between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

    # Pack into a tuple and append
    tasks.append((title, priority))
    print("Task added.\n")
# Complete task - remove from list
def complete_tasks(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Task number to complete: ").strip())
        # Convert to zero-based index
        task = tasks.pop(idx - 1)
        print(f"Completed: {task[0]} (priority {task[1]})")
    except (ValueError, IndexError):
        print("Invalid task number.")
# Show number of remaining tasks
def show_top(tasks):
    if not tasks:
        print("No tasks found")
        return
    try:
        n = int(input("Number of tasks to show: "))
        if n <= 0:
            print("Please enter a positive number")
            return
        # Sort a copy by priority ascending; lower number = higher priority
        sorted_copy = sorted(tasks, key=lambda t: t[1])
        top_n = sorted_copy[:n] # slicing
        print(f"Top {n} tasks:")
        for idx, (title, priority) in enumerate(top_n, start=1):
            print(f"{idx}. {title} (priority {priority})")
            print()
    except ValueError:
        print("Please enter a valid number")

############################################################################################
# Testing Functions
# tasks = [("Push repository",3),("Fight the power", 6), ("Chillax", 1),("Save humans", 7)]
# print(type(tasks))
# show_tasks(tasks)
# add_tasks(tasks)
# show_tasks(tasks)
# complete_tasks(tasks)
# show_tasks(tasks)
# show_top(tasks)
############################################################################################

def main():
    tasks = []
    actions = {
        "1": add_tasks,
        "2": complete_tasks,
        "3": show_tasks,
        "4": show_top,

    }

    while True:
        print("To-Do List Manage")
        print("1. Add task")
        print("2. Complete task")
        print("3. Show tasks")
        print("4. Show top N tasks")
        print("q. Quit")
        choice = input("Choice: ")
        if choice == "q":
            print("Goodbye")
            break
        elif choice in actions:
            if choice in {"3"}:
                actions[choice](tasks)
            else:
                actions[choice](tasks)
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()


