import pytest

from src.user import User
from src.task import Task
from src.task_iterator import TaskIterator
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask


@pytest.fixture
def first_user():
    return User(
        username = "User",
        email = "user@mail.ru",
        first_name = "User",
        last_name = "Userov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", run_time=60),
            Task("Купить билеты", "Купить билеты на самолет", run_time=60),
            Task("Купить телевизор", "Купить телевизор в магазине", run_time=60)
        ]
    )

@pytest.fixture
def second_user():
    return User(
        username="Ivan",
        email="ivan@mail.com",
        first_name="Ivan",
        last_name="Olegov",
        task_list=[
            Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2025"),
            Task("Купить помидоры", "Купить помидоры для салата", created_at="20.04.2025"),
            Task("Купить лук", "Купить лук для салата", created_at="20.04.2025")
        ]
    )


@pytest.fixture
def task():
    """Фикстура для новой задачи"""
    return Task("Купить огурцы", "Купить огурцы для салата", created_at="20.04.2025", run_time=60)


@pytest.fixture
def task_with_runtime1():
    """Фикстура с задачей, которая содержат время выполнения задачи1 run_time"""
    return Task("Купить помидоры", "Купить помидоры для салата", created_at="20.04.2025", run_time=60)


@pytest.fixture
def task_with_runtime2():
    """Фикстура с задачей, которая содержат время выполнения задачи2 run_time"""
    return Task("Купить перец", "Купить перец для салата", created_at="20.04.2025", run_time=70)


@pytest.fixture
def task_iterator(second_user):
    """Фикстура с готовым итератором для пользователя `second_user` (данные - из фикстуры second_user)"""
    return TaskIterator(second_user)


@pytest.fixture
def task_periodic_1():
    """Фикстура с периодической задачей для класса PeriodicTask"""
    return PeriodicTask("Купить огурцы", "Купить огурцы для салата", "01.04.2025", "01.06.2025", created_at="20.04.2025", run_time=60)


@pytest.fixture
def task_periodic_2():
    """Фикстура с периодической задачей для класса PeriodicTask"""
    return PeriodicTask("Купить лук", "Купить лук для салата", "01.04.2025", "01.06.2025", created_at="20.04.2025", run_time=60)


@pytest.fixture
def task_deadline_1():
    """Фикстура со сроком выполнения задачи для класса DeadlineTask"""
    return DeadlineTask("Купить перец", "Купить перец для салата", "20.05.2025", created_at="20.04.2025", run_time=60)


@pytest.fixture
def task_deadline_2():
    """Фикстура со сроком выполнения задачи для класса DeadlineTask"""
    return DeadlineTask("Купить оливки", "Купить оливки для салата", "20.05.2025", created_at="20.04.2025", run_time=60)


@pytest.fixture
def user_without_tasks():
    return User(
        username="Some",
        email="some.com",
        first_name="Some",
        last_name="User",
    )


