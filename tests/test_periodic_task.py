import pytest


def test_periodic_task_init(task_periodic_1):
    assert task_periodic_1.name == "Купить огурцы"
    assert task_periodic_1.description == "Купить огурцы для салата"
    assert task_periodic_1.start_date == "01.04.2025"
    assert task_periodic_1.end_date == "01.06.2025"
    assert task_periodic_1.created_at == "30.05.2025"

def test_periodic_task_add(task_periodic_1, task_periodic_2):
    assert task_periodic_1 + task_periodic_2 == 120

def test_periodic_task_error(task_periodic_1, task_periodic_2):
    with pytest.raises(TypeError):
        assert task_periodic_1 + 1
