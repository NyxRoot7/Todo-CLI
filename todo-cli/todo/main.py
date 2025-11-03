from todo.storage import add_task, remove_task, load_tasks

def show_menu():
    print("\n=== TODO CLI ===")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            tasks = load_tasks()
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
            print("Task added!")
        elif choice == "3":
            index = int(input("Enter task number to remove: ")) - 1
            removed = remove_task(index)
            if removed:
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
