import json 
import os

def load_tasks():
    if not os.path.exists(tasks.json):
        return {"tasks:[]"} # create empty structure if file doesn't exists
    
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        
def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=2)
'''Use the json module's dump() function to serialize the modified Python object back into JSON format and write it to the file. 
It's good practice to use indent for readability.
'''


        
def add(title):
    tasks = load_tasks()
    tasks_list = tasks["tasks"]
    
    new_id = 1 if not tasks_list else tasks_list[-1]["id"]+1
    
    new_task = {
        "id": new_id,
        "title": title,
        "status": False
    }
    
    tasks_list.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def show():
    tasks = load_tasks
    
    if not tasks["tasks"]:
        print("Task List empty.")
        return
    
    print("\nYour Tasks: ")
    for task in tasks["tasks"]:
        status = "✔ Done" if task["status"] else "✗ Not done"
        print(f"{task['id']}. {task['title']} - {status}")
    print()
        
def mark_done(task_id):
    tasks = load_tasks
    
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            task['status'] = True
            save_tasks(tasks)
            print(f"Task {task_id} is marked as complete!")
            return
        
    print("Task not found!")
    
'''
To delete an object from a JSON file using Python, 
the general approach involves reading the JSON data into a Python object (usually a dictionary or a list of dictionaries), 
modifying that Python object to remove the desired item, and then writing the updated Python object back to the JSON file.
'''    
def delete(task_id):
    tasks = load_tasks()
    tasks_list = tasks["tasks"]
    
    new_list = [task for task in tasks_list if task['id'] != task_id]
    
    if len(new_list) == len(tasks_list):
        print("Task not found!")
        return 
    
    tasks['tasks'] = new_list
    save_tasks(tasks)
    print(f"Task {task_id} deleted!")