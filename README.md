## 1. Simple Calculator
    # Concepts : Variables, Data Types, Basic Operatirs, Functions, Input/Output
    # Objective: Create a basic calculator that can perform addition, subtraction, multiplicarion and division.

## 2. To Do application (commandline)
    # Concepts    : List, Loops, Conditionals, Basic Error Handeling (Try, Except).
    # Objective   : Build a CLI-Based to-do list manager where users can add, view and remove tasks.
    # Instructions: 
                1. Set up basic strecture:-> Create and empty list to store tasks.
                2. Create a Menu---------:-> Use a while loop to display a menu with options> Add Task, View Task, Remove Task, and Exit.
                3. Add Tasks-------------:-> Create a function to add a new task by appending it to the list.
                4. View Tasks------------:-> Display all tasks using a loop.
                5. Remove/Complete Tasks-:-> Implement a function to delete a task based on its index or name.
                6. Implement Exit--------:-> Allow user to exit the loop.

## 3. REST API building ( CLI and POSTMAN )
    # Concepts : FLASK, function, class, methods, sqlite3, librairies
    # Objective: Build an api which can do CRUD functrion in a database using postman (postman requests will hit routes that will work on database)

## 4. Weather App with API (CLI) [ api.openweathermap.org ]
    # Concepts    : Libraries, APIs, JSON Parsing, Exception Handling
    # Objective   : Build a weather app that fetches data from an API to display the current weather
    # Instructions: 
                1. Signup for API Access-------:-> Get an API key from a weather service provider (e.g.,OpenWeatherMap)
                2. Install Required Libraries--:-> Use pip to install requests.
                3. Make an API Request---------:-> Use the request library to fetch weather data by city or location.
                4. Parse JSON Data-------------:-> Extract necessary data (e.g., temperature, weather condition) from the JSON response.
                5. Display Weather Information-:-> Print the extracted weather information.
                6. Error Handling--------------:-> Handle cases like incorrect city names or API limits.

## 5. Personal Expense Tracker
    # Concepts   : File Handling, CSV Operations, Data Persistence(storing data and keeping it alive).
    # Objective  : Create a program to track expenses and income, saving data to a CSV file for future reference.
    # Instruction: 
                1. Set Up CSV File--:-> Create a CSV file (expenses.csv) with columns for Data,Description, Category, and Amount.
                2. Create Functions-:-> i. add_expense : Adds a new record to the CSV file.
                                       ii. view_expense: Reads and displays data from the CSV file.
                3. Take User Input--:-> Allow users to enter details for each expense.
                4. Save to CSV------:-> Use Python's csv module to write entries to the file.
                5. Read from CSV----:-> Use csv.reader to display all saved entries.
                6. Error Handling---:-> Handle any file-related errors, such as missing files or invalid entris.
