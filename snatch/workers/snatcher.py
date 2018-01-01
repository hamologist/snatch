from abc import abstractmethod, ABCMeta

from snatch.workers.context import Context


class SnatcherContext(metaclass=ABCMeta):
    pass


class Snatcher(metaclass=ABCMeta):

    @abstractmethod
    def run(self, context: Context) -> SnatcherContext:
        pass
