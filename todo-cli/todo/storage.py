import os

FILE_PATH = "todo_data.txt"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        f.write("\n".join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        return removed
    except IndexError:
        return None
