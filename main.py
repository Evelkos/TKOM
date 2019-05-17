# main.py

import sys
from src.lexer import Lexer
from src.token import Type
from src.source import Source
from src.parser import Parser
from src.visitor import Visitor
from src.interpreter import Interpreter

if __name__ == "__main__":
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    visitor = Visitor()
    interpreter = Interpreter(parser, visitor)
    interpreter.run()

    # functions = parser.parse()

    # for function in functions:
    #     print()
    #     print(function)
