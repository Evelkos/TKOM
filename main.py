# main.py

import sys
from src.lexer import Lexer
from src.token import Type

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        file = open(filename, "r")
        file.close()
        
        lexer = Lexer(filename)
        while lexer.get_token().get_type() != Type.EOF:
            lexer.build_next_token()
            print(lexer.get_token())
    except:
        print("Podano zla nazwe pliku")
        exit(1)