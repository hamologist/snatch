from abc import ABCMeta, abstractmethod
from typing import Type, TypeVar, Generic, Union

from snatch.workers.context import Context
from snatch.workers.processor import Processor
from snatch.workers.snatcher import Snatcher

Snatcher_Type = TypeVar('Snatcher_Type')
Processor_Type = TypeVar('Processor_Type')


class Worker(Generic[Snatcher_Type, Processor_Type], metaclass=ABCMeta):

    @property
    @abstractmethod
    def snatcher_type(self) -> Type[Snatcher_Type]:
        pass

    @property
    @abstractmethod
    def processor_type(self) -> Type[Processor_Type]:
        pass

    def __init__(self, context: Context):
        self.context: Context = context
        self.snatcher: Union[Snatcher_Type, Snatcher] = self.snatcher_type()
        self.processor: Union[Processor_Type, Processor] = self.processor_type()

    def run(self):
        context = self.context

        snatcher_context = self.snatcher.run(context)
        self.processor.run(context, snatcher_context)