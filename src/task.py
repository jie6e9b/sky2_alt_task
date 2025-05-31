# Продолжение работы над альтернативной задачей по теме "Классы"

import datetime
from src.base_task import BaseTask
from src.print_mixin import PrintMixin


class Task(BaseTask, PrintMixin):
    name: str
    description: str
    status: str
    created_at: str
    run_time: int  # Время выполнения задачи в минутах

    def __init__(self, name, description, status="Ожидает старта", created_at=None, run_time=0):
        self.name = name
        self.description = description
        self.status = status
        # Атрибут `created_at` сделали приватным
        self.__created_at = created_at if created_at else datetime.date.today().strftime("%d.%m.%Y")
        if run_time >= 0:
            self.run_time = run_time  # Время выполнения задачи
        else:
            raise ValueError("Задачу с отрицательным временем выполнения создать нельзя")
        super().__init__()  # Вызов __init__ и __repr__ у миксина PrintMixin



    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.__created_at}"


    def __add__(self, other):
        if type(other) is Task:
            return self.run_time + other.run_time
        raise TypeError

    @classmethod
    def new_task(cls, name, description, status="Ожидает старта", created_at = None):
        """Метод класса, который принимает на вход параметры и создает новую задачу.
        Возвращает новый экземпляр класса Task"""

        # cls ссылается на класс Task, что эквивалентно записи Task(name, ...).
        # Соответственно, при этом создается новый экземпляр класса Task
        return cls(name, description, status, created_at)

    @property
    def created_at(self):
        """Геттер. Возвращает значение приватного атрибута `created_at`"""
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        """Сеттер. Изменяет значение приватного атрибута `created_at` на новое (передается в виде строки)"""
        # Выполняется проверка, что переданная дата для создания новой задачи не меньше текущей. Предварительно
        # преобразовать переданную дату в datetime (время отбрасывается)
        if datetime.datetime.strptime(new_date, "%d.%m.%Y").date() < datetime.date.today():
            print("Нельзя изменить дату создания на дату из прошлого")
            return  # Выводится предупреждение и завершается работа метода

        self.__created_at = new_date  # Если проверка прошла, то переприсваиваем приватный атрибут `created_at`


if __name__== "__main__":
    task_1 = Task("Купить огурцы", "Купить огурцы для салата", run_time=60)  # При этом вызовется метод

    # __repr__ из класса PrintMixin

    print(task_1.name)
    print(task_1.description)
    print(task_1.status)
    print(task_1.created_at)
    print()  # Пустая строка

    # Создание новой задачи. Обращаемся к классу `Task` и вызываем метод `new_task` этого класса. Вывод новых атрибутов
    task_2 = Task.new_task("Купить билеты", "Купить билеты на самолет")  # При этом вызовется метод
    # __repr__ из класса PrintMixin

    print(task_2.name)
    print(task_2.description)
    print(task_2.status)
    print(task_2.created_at)
    print()  # Пустая строка

    # Задаем новую дату (из прошлого)
    task_2.created_at = "01.04.2025"   # Получаем "Нельзя изменить дату создания на дату из прошлого".
    print(task_2.created_at)   # Атрибут не изменяется

    # Задаем новую дату (для будущего)
    task_2.created_at = "01.12.2025"
    print(task_2.created_at)   # Получаем новое значение атрибута `created_at` (01.12.2025)

    print(task_1 + task_2)
    print()  # Пустая строка

    # task = Task("Купить огурцы", "Купить огурцы для салата", run_time=-60)  # При этом вызовется метод

    #
    # # Проверка на сложение объекта класса Task с объектом другого класса
    # print(task_1 + 1)  #  TypeError, т.к. разные классы у объектов