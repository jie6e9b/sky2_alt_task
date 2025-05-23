import json
import os
from pprint import pprint

from src.user import User
from src.task import Task


def read_json(path: str) -> dict:
    """Функция чтения JSON-файла"""
    full_path = os.path.abspath(path)  # Полный путь к JSON-файлу
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data


def create_objects_from_json(data):
    users = []
    for user in data:
        tasks = []
        for task in user["task_list"]:
            tasks.append(Task(**task))  # Распаковка словарей под ключом user['task_list']
        user["task_list"] = tasks  # Вместо списка словарей по ключу user['task_list'] будет находиться список
        # экземпляров класса Task
        users.append(User(**user))

    return users


if __name__== "__main__":
    raw_data = read_json("../data/data.json")
    pprint(raw_data)

    users_data = create_objects_from_json(raw_data)
    print(users_data)

    print(users_data[0].username)
    print(users_data[0].task_list)