class Task:
    def __init__(self):
        self.task_name = ""
        self.priority = ""
        self.completed = False

    def set_task_detail(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority

    def mark_as_complete(self):
        self.completed = True

    def display_task_info(self):
        status = "Completed" if self.completed else "Not Completed"
        print("Task:", self.task_name)
        print("Priority:", self.priority)
        print("Status:", status)
        print()

if __name__ == "__main__":
    task_list = []

    # Create an object of the Task class
    task = Task()

    # Set task details
    task.set_task_detail("Buy groceries", "High")
    task_list.append(task)

    # Mark the task as completed
    task.mark_as_complete()

    # Display task information
    for t in task_list:
        t.display_task_info()
