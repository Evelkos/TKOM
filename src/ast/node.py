# node.py
from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def visit(self):
        pass