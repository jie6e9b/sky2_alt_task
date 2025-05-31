import pytest

def test_deadline_task_init(task_deadline_1):
    """Тест инициализации класса DeadlineTask"""
    assert task_deadline_1.name == "Купить перец"
    assert task_deadline_1.description == "Купить перец для салата"
    assert task_deadline_1.deadline == "20.05.2025"
    assert task_deadline_1.status == "Ожидает старта"
    assert task_deadline_1.created_at == "20.04.2025"
    assert task_deadline_1.run_time == 60


def test_deadline_task_add(task_deadline_1, task_deadline_2):
    """Тест на сложение объектов (времени выполнения задачи) класса PeriodicTask с использованием фикстур task_deadline_1(2)"""
    assert task_deadline_1 + task_deadline_2 == 120


def test_deadline_task_add_error(task_deadline_1):
    """Тест на сложение объекта (времени выполнения задачи) класса DeadlineTask (с использованием фикстуры task_deadline_1) и другого класса"""
    with pytest.raises(TypeError):
        assert task_deadline_1 + 1