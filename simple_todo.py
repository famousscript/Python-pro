"""
Simple To-Do List (Console)
A basic console application for managing tasks
"""

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*30)
    print("    SIMPLE TO-DO LIST")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("="*30)

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    """Display all tasks"""
    print("\n--- YOUR TASKS ---")
    if not tasks:
        print("No tasks found. Your list is empty!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks):
    """Delete a task from the list"""
    if not tasks:
        print("No tasks to delete. Your list is empty!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main application loop"""
    tasks = []  # List to store tasks
    
    print("Welcome to Simple To-Do List!")
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Thank you for using Simple To-Do List! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()