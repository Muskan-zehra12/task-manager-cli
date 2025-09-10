import sys

tasks = []

// this function adds a task to the task list created by muskan
def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

// this function lists all tasks created by mukarram
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")




if __name__ == "__main__":
    command = sys.argv[1]
    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "show":
        show_tasks()
    elif command == "delete":
        delete_task(int(sys.argv[2]))
    else:
        print("Unknown command")