import json as js
class todolist():
    def __init__(self):
        # Load existing tasks
        try:
            with open("data.json", "r") as file:
                self.data = js.load(file)
        except (FileNotFoundError, js.JSONDecodeError):
            self.data = []

    def save(self):
        with open("data.json", "w") as file:
            js.dump(self.data, file, indent=4)

    def task(self):

        while True:
            print("\n--- To Do List ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark a Task as Done")
            print("4. Delete a Task")
            print("5. Save & Exit")

            try:
                choice = int(input("Choose option: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue   # go back to menu

            if choice == 1:
                task = input("Enter Task: ")
                self.data.append(task)   # ✅ add task to the list
                with open("data.json", "w") as file:
                    js.dump(self.data, file, indent=4)   # ✅ save entire list
                print("Task added!")
            elif choice == 2:
                if not self.data:
                    print("No tasks added yet!")
                else:
                    for i, t in enumerate(self.data, start=1):
                        print(f"{i}. {t}")
            elif choice == 3:
                if not self.data:
                    print("No tasks to mark!")
                else:
                    for i, t in enumerate(self.data, start=1):
                        print(f"{i}. {t}")
                    num = int(input("Enter task number to mark as done: "))
                    if 0 < num <= len(self.data):
                        self.data[num - 1] = self.data[num - 1] + " ✅"
                        with open("data.json", "w") as file:
                            js.dump(self.data, file, indent=4)   # ✅ save entire list
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
            elif choice == 4:
                if not self.data:
                    print("No tasks to delete!")
                else:
                    for i, t in enumerate(self.data, start=1):
                        print(f"{i}. {t}")
                    num = int(input("Enter task number to delete: "))
                    if 0 < num <= len(self.data):
                        removed = self.data.pop(num - 1)
                        with open("data.json", "w") as file:
                            js.dump(self.data, file, indent=4)   # ✅ save entire list
                        print(f"Task '{removed}' removed!")
                    else:
                        print("Invalid task number.")
            elif choice == 5:
                with open("data.json", "w") as file:
                    js.dump(self.data, file, indent=4)
                print("Tasks saved! Exiting...")
                break

obj = todolist()
print(obj.task())