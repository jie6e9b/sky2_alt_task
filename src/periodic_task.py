from src.task import Task

class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date, status="Ожидает старта", created_at=None, run_time=0, frequency="Ежедневная"):
        super().__init__(name, description, status="Ожидает старта", created_at=None, run_time=60)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if type(other) is PeriodicTask:
            return self.run_time + other.run_time
        raise TypeError

if __name__ == "__main__":
    periodic_task = PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.01.2020","01.01.2026", run_time=60)
    task_1 = PeriodicTask("Купить огурцы", "Купить огурцы для салата", "05.05.2025","05.05.2030", run_time=60)  # При этом вызовется метод

    print(periodic_task + task_1)

    print(periodic_task.name)
    print(periodic_task.description)
    print(periodic_task.status)
    print(periodic_task.created_at)
    print(periodic_task.start_date)
    print(periodic_task.end_date)
    print(periodic_task.frequency)

