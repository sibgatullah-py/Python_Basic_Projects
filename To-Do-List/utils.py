import json
import os

class Management:

    @staticmethod
    def load_tasks():
        if not os.path.exists("tasks.json"):
            return {"tasks": []}  # empty template

        with open("tasks.json", "r") as file:
            return json.load(file)

    @staticmethod
    def save_tasks(tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=2)


    @staticmethod
    def add(title):
        tasks = Management.load_tasks()
        tasks_list = tasks["tasks"]

        new_id = 1 if not tasks_list else tasks_list[-1]["id"] + 1

        new_task = {
            "id": new_id,
            "title": title,
            "status": False
        }

        tasks_list.append(new_task)
        Management.save_tasks(tasks)
        print(f"Task added: {title}")


    @staticmethod
    def show():
        tasks = Management.load_tasks()

        if not tasks["tasks"]:
            print("Task List empty.")
            return

        print("\nYour Tasks:")
        for task in tasks["tasks"]:
            status = "✔ Done" if task["status"] else "✗ Not done"
            print(f"{task['id']}. {task['title']} - {status}")
        print()


    @staticmethod
    def mark_done(task_id):
        tasks = Management.load_tasks()

        for task in tasks["tasks"]:
            if task["id"] == task_id:
                task["status"] = True
                Management.save_tasks(tasks)
                print(f"Task {task_id} is marked as complete!")
                return

        print("Task not found!")


    @staticmethod
    def delete(task_id):
        tasks = Management.load_tasks()
        tasks_list = tasks["tasks"]

        new_list = [task for task in tasks_list if task["id"] != task_id]

        if len(new_list) == len(tasks_list):
            print("Task not found!")
            return

        tasks["tasks"] = new_list
        Management.save_tasks(tasks)
        print(f"Task {task_id} deleted!")
