# lexer.py

from source import Source
from token import Token, Type

class Lexer:
    def __init__(self, filename = "../test/test.txt"):
        self.source = Source(filename)
        self.token = Token()


    def build_next_token(self):
        self.ignore_white_spaces()
        if not self.try_eof():
            if not self.try_identifier():
                self.try_digit()


    def get_token(self):
        return self.token


    def ignore_white_spaces(self):
        while self.source.get_char() == " " or self.source.get_char() == "\n":
            self.source.get_next_char()


    def read_identifier(self):
        character = self.source.get_char()
        buff = ""

        if character.isalpha():
            while character.isalpha() or character.isdigit():
                buff += character
                character = self.source.get_next_char()
        return buff


    def read_number(self):
        character = self.source.get_char()
        buff = ""

        if character.isdigit():
            while character.isdigit():
                buff += character
                character = self.source.get_next_char()
        return buff


    def try_eof(self):
        character = self.source.get_char()

        if character is "":
            self.token = Token(Type.EOF, None)
            return True
        return False


    def try_digit(self):
        token_value = self.read_number()
        if token_value != "":
            self.token = Token(Type.NUMBER, token_value)
            return True
        return False


    def try_identifier(self):
        token_value = self.read_identifier()
        # tu dorobic sprawdzenie, czy slowo nie jest slowem kluczowym
        if token_value != "":
            self.token = Token(Type.IDENTIFIER, token_value)
            return True
        return False


lexer = Lexer("../test/test.txt")
while lexer.get_token().get_type() != Type.EOF:
    lexer.build_next_token()
    print(lexer.get_token())