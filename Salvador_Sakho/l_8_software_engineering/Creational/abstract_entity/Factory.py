from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_robot(self, robot):
        pass
