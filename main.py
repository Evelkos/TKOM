# main.py
import sys
from src.lexer import Lexer
from src.source import Source
from src.parser import Parser
from src.visitor import Visitor
from src.interpreter import Interpreter
from src.exceptions import (
    InvalidSyntax,
    UndefinedOperation,
    InvalidOperation,
    Undeclared,
    InvalidValue
)


if __name__ == "__main__":
    source = Source(sys.stdin)
    lexer = Lexer(source)
    parser = Parser(source, lexer)
    visitor = Visitor()
    interpreter = Interpreter(parser, visitor)
    try:
        result = interpreter.run()
        print(f"Ostateczny wynik = {result}")
    except InvalidSyntax as e:
        print(
            f"Error: On position: {e.position}. "
            f"Expected {e.expected_type}, but "
            f"got {e.given_type}: {e.given_value}.")
    except UndefinedOperation as e:
        print(
            f"Error: Undefined operation {e.operation} for "
            f"left operand with type {e.left_operand} and "
            f"right operand with type {e.right_operand}."
        )
    except InvalidOperation as e:
        print(
            f"Error: Invalid operation {e.operation} with {e.left_operand} "
            f"and {e.right_operand}."
        )
    except Undeclared as e:
        print(f"Error: Undeclared {e.subject} with name {e.name}.")
    except InvalidValue as e:
        print(f"Error: Expected {e.expected_type}, got {e.given_type}.")
