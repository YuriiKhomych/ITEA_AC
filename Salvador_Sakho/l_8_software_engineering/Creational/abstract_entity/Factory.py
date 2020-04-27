from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_robot(self, robot):
        pass

    @abstractmethod
    def add_new_model(self, robot):
        pass
