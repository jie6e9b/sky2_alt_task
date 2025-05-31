from src.task import Task

class DeadlineTask(Task):
    def __init__(self, name, description, deadline, status="Ожидает старта", created_at=None, run_time=0, frequency="Ежедневная"):
        super().__init__(name, description, status, created_at, run_time)
        self.deadline = deadline

    def __add__(self, other):
        if type(other) is DeadlineTask:
            return self.run_time + other.run_time
        raise TypeError

if __name__ == "__main__":
    deadline_task = DeadlineTask("Купить огурцы", "Купить огурцы для салата", "01.01.2020")

    print(deadline_task.name)
    print(deadline_task.description)
    print(deadline_task.status)
    print(deadline_task.created_at)
    print(deadline_task.deadline)

