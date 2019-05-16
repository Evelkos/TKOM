# node.py
from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def __init__(self, line=None, column=None):
    	self.line = line
    	self.column = column

    def visit(self):
        pass