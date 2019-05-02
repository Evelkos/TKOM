# main.py

import sys
from src.lexer import Lexer
from src.token import Type
from src.source import Source

if __name__ == "__main__":
    source = Source()
    lexer = Lexer(source)
    while lexer.get_token().get_type() != Type.EOF:
        lexer.build_next_token()
        print(lexer.get_token())
