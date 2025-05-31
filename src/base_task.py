from abc import ABC, abstractmethod


class BaseTask(ABC):

    @classmethod
    @abstractmethod
    def new_task(cls, *args, **kwargs):
        pass
