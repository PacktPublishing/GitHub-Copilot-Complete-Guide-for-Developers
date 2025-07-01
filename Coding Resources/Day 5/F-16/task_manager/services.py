from models import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)
        return task

    def update_task(self, task_id, title=None, description=None, completed=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if completed is not None:
                    task.completed = completed
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return task
        return None

    def list_tasks(self):
        return self.tasks