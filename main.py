# main.py

import sys
from src.lexer import Lexer
from src.token import Type
from src.source import Source
from src.parser import Parser
from src.visitor import Visitor
from src.interpreter import Interpreter
from src.exceptions import InvalidSyntax

if __name__ == "__main__":
    source = Source()
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    visitor = Visitor()
    interpreter = Interpreter(parser, visitor)
    try:
        interpreter.run()
    except InvalidSyntax as e:
        print(
            f"Error on position: {e.position}. "
            f"Expected {e.expected_type}, but "
            f"got {e.given_type}: {e.given_value}")
