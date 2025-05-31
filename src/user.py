from src.exceptions import ZeroRuntimeTask
from src.task import Task


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0


    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []  # Атрибут `task_list` сделали приватным

        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0  # Счетчик количества задач будет увеличиваться
        # на длину списка задач, если он существует. Если список пустой, тогда не увеличивается


    def __str__(self):
        """Строковое представление экземпляра класса User"""
        return f"{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}"


    @property
    def task_list(self):
        """Геттер. Возвращает новую строку (тип str), содержащую подстроки из списка задач"""
        task_str = ""
        for task in self.__task_list:  # Перебор списка задач
            task_str += f"{str(task)}\n" # Представление задачи (объекта класса Task) в строковом формате путем вызова
            # магического метода def __str__(self) из класса Task
        return task_str

    @task_list.setter
    def task_list(self, new_task: Task):      # new_task - передаем новую задачу (тип - экземпляр класса Task)
        """Сеттер. Дополняет список задач новой задачей"""
        if isinstance(new_task, Task):  # Если полученная новая задача принадлежит классу Task или его наследнику, то она добавляется в список задач
            try:
                if new_task.run_time == 0:
                    raise ZeroRuntimeTask("Нельзя задать задачу с нулевым временем выполнения")
            except ZeroRuntimeTask as error_info:
                print(error_info)
            else:
                self.__task_list.append(new_task)
                User.all_tasks_count += 1  # Увеличиваем значение количества всех задач на 1
                print("Задача добавлена успешно")
            finally:
                print("Обработка добавления задачи завершена")
        else:
            raise TypeError("Попытка добавления несовместимого типа данных")

    @property
    def task_in_list(self):
        """Геттер. Возвращает список задач (тип list). Нужен для чтения(только!) содержимого приватного атрибута __task_list"""
        return self.__task_list

    def middle_task_runtime(self):
        """Метод для определения среднего времени выполнения всех задач объекта класса User"""
        try:
            return sum([task.run_time for task in self.__task_list]) / len(self.__task_list)
        except ZeroDivisionError:
            return 0

if __name__== "__main__":
    # Создаем 4 новых задачи
    task_1 = Task("Купить огурцы", "Купить огурцы для салата", run_time=20)
    task_2 = Task("Купить помидоры", "Купить помидоры для салата", run_time=30)
    task_3 = Task("Купить лук", "Купить лук для салата", run_time=20)
    task_4 = Task("Купить перец", "Купить перец для салата", run_time=50)

    # Создаем 1 нового пользователя
    user = User("OleJik", "oleg@mail.com", "Oleg", "Ivanov", [task_1, task_2, task_3, task_4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(User.all_tasks_count)

    # Добавление новой задачи и вывод обновленного списка задач и количества всех задач
    task_5 = Task("Купить рукколу", "Купить рукколу для салата")
    user.task_list = task_5  # Вызов сеттера `task_list`
    print(user.task_list)
    print(User.all_tasks_count)

    print(user)
    print(user.middle_task_runtime())
    user1 = User("OleJik", "oleg@mail.com", "Oleg", "Ivanov", [])
    print(user1.middle_task_runtime())