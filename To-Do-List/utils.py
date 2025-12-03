import json
import os

class Management:

    def load_tasks(self):
        if not os.path.exists("tasks.json"):
            return {"tasks": []}  # empty template

        with open("tasks.json", "r") as file:
            return json.load(file)

    def save_tasks(self, tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=2)

    def add(self, title):
        tasks = self.load_tasks()
        tasks_list = tasks["tasks"]

        new_id = 1 if not tasks_list else tasks_list[-1]["id"] + 1

        new_task = {
            "id": new_id,
            "title": title,
            "status": False
        }

        tasks_list.append(new_task)
        self.save_tasks(tasks)
        print(f"Task added: {title}")

    def show(self):
        tasks = self.load_tasks()

        if not tasks["tasks"]:
            print("Task List empty.")
            return

        print("\nYour Tasks:")
        for task in tasks["tasks"]:
            status = "✔ Done" if task["status"] else "✗ Not done"
            print(f"{task['id']}. {task['title']} - {status}")
        print()

    def mark_done(self, task_id):
        tasks = self.load_tasks()

        for task in tasks["tasks"]:
            if task["id"] == task_id:
                task["status"] = True
                self.save_tasks(tasks)
                print(f"Task {task_id} is marked as complete!")
                return

        print("Task not found!")

    def delete(self, task_id):
        tasks = self.load_tasks()
        tasks_list = tasks["tasks"]

        new_list = [task for task in tasks_list if task["id"] != task_id]

        if len(new_list) == len(tasks_list):
            print("Task not found!")
            return

        tasks["tasks"] = new_list
        self.save_tasks(tasks)
        print(f"Task {task_id} deleted!")
