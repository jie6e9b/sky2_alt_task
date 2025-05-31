import pytest
from src.task import Task

def test_user_init(first_user, second_user):
    """Тест инициализации класса user"""
    assert first_user.username == "User"
    assert first_user.email == "user@mail.ru"
    assert first_user.first_name == "User"
    assert first_user.last_name == "Userov"
    assert len(first_user.task_in_list) == 2


    assert second_user.username == "Ivan"
    assert second_user.email == "ivan@mail.com"
    assert second_user.first_name == "Ivan"
    assert second_user.last_name == "Olegov"

    assert first_user.users_count == 2
    assert second_user.users_count == 2

def test_user_task_list_setter_error(first_user):
    """"Тест сеттера `user.task_list` на сложение объекта класса Task c объектом другого класса"""
    with pytest.raises(TypeError):
        first_user.task_list = 1

def test_user_task_list_setter_periodic_task(first_user, task_periodic_1):
    """"Тест сеттера `user.task_list` на сложение родственных объектов класса Task и PeriodicTask"""
    first_user.task_list = task_periodic_1
    assert first_user.task_in_list[-1].name == "Купить огурцы"  # Проверка, что новая задача добавлена в список задач



