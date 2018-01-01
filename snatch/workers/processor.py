from abc import ABCMeta, abstractmethod

from snatch.workers.context import Context
from snatch.workers.snatcher import SnatcherContext


class Processor(metaclass=ABCMeta):

    @abstractmethod
    def run(self, context: Context, snatcher_context: SnatcherContext):
        pass
