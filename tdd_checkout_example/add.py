from abc import ABC, abstractmethod


class AbstractAdder(ABC):
    @abstractmethod
    def add(self, value1, value2):
        pass


class ConcreteAdder(AbstractAdder):
    def add(self, value1, value2):
        return value1 + value2


def AddExecutor(AbstractAdder):
    return AbstractAdder.add(1, 2)
