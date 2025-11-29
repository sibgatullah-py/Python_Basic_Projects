from utils import Management
import os

def clear(): # clear screen method
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            Management.add(title)

        elif choice == "2":
            Management.show()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark done: "))
                Management.mark_done(task_id)
            except ValueError:
                print("Invalid ID! Only numbers allowed.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                Management.delete(task_id)
            except ValueError:
                print("Invalid ID! Only numbers allowed.")

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please choose between 1-5.")
            
        input("\nPress Enter to continue...")  # Wait before clearing
        clear()  # Clear AFTER result

if __name__ == "__main__":
    main_menu()
