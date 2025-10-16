from abc import ABC, abstractmethod


class PoolStrategy(ABC):
    @abstractmethod
    def run(self):
        pass
