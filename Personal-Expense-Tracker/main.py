from utils import Backend
import os

Backend = Backend()

def clear(): # clear screen method
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    Backend.initialize_csv()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            Backend.add_expense(date, description, category, amount)

        elif choice == "2":
            Backend.view_expenses()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")
        
        input("\nPress Enter to continue...")
        clear()

if __name__ == "__main__":
    main()