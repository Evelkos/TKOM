# interpreter.py

from .lexer import Lexer
from .source import Source
from .parser import Parser
from .visitor import Visitor


class Interpreter():
    def __init__(self, parser, visitor):
        self.parser = parser
        self.visitor = visitor

    def run(self):
        functions = self.parser.parse()
        self.visitor.set_functions_def(functions)
        
        for function in functions:
            if (function.identifier.name == "main"):
                print(function)
                function.accept(self.visitor)
