# lexer.py

from source import Source
from token import Token, Type, Symbol

class Lexer:
    def __init__(self, filename = "../test/test.txt"):
        self.source = Source(filename)
        self.token = Token()


    def build_next_token(self):
        self.ignore_white_spaces()
        if self.try_eof():
            return
        elif self.try_identifier():
            return
        elif self.try_digit():
            return
        elif self.try_single_characters():
            return
        else:
            return


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
        word = self.read_identifier()
        try:
            token_type = Symbol.key_words[word]
            self.token = Token(token_type, word)
            self.source.get_next_char()
            return True
        except:
            if word != "":
                self.token = Token(Type.IDENTIFIER, word)
                self.source.get_next_char()
                return True
            return False


    def try_single_characters(self):
        character = self.source.get_char()
        try:
            token_type = Symbol.special_characters[character]
            self.token = Token(token_type, character)
            self.source.get_next_char()
            return True
        except:
            return False


lexer = Lexer("../test/test.txt")
while lexer.get_token().get_type() != Type.EOF:
    lexer.build_next_token()
    print(lexer.get_token())