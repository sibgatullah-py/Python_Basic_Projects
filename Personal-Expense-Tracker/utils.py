import csv
import os

CSV_FILE = "expenses.csv"

class Backend:
    # Ensure CSV file exists with headers
    def initialize_csv(self):
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Description", "Category", "Amount"])
                
    # Adds a new record
    def add_expense(self, date, description, category, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Enter a number.")
            return

        try:
            with open(CSV_FILE, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date, description, category, amount])
            print("Expense added successfully!\n")

        except Exception as e:
            print(f"Error writing to file: {e}")

    # Views all the records
    def view_expenses(self):
        try:
            with open(CSV_FILE, "r") as file:
                reader = csv.reader(file)
                rows = list(reader)

            if len(rows) <= 1:
                print("No expenses found.\n")
                return

            print("\n--- Saved Expenses ---")
            for row in rows:
                print(row)
            print()

        except FileNotFoundError:
            print("File not found. Creating a new CSV...")
            self.initialize_csv()

        except Exception as e:
            print(f"Error reading file: {e}")
