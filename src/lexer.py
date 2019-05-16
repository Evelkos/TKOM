# lexer.py

from .source import Source
from .token import Token, Type, Symbol


class Lexer:
    def __init__(self, source):
        self.source = source
        self.token = Token()


    def build_next_token(self):
        self.ignore_white_spaces()
        if self.try_eof():
            return
        elif self.try_identifier():
            return
        elif self.try_digit():
            return
        elif self.try_double_operator():
            return
        elif self.try_single_character():
            return
        else:
            self.token = Token(Type.UNIDENTIFIED, self.source.get_char())
            self.source.get_next_char()
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

        if character == '0':
            buff += character
            character = self.source.get_next_char()

        elif character.isdigit() and character != '0':
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

    def try_double_operator(self):
        character = self.source.get_char()
        if character == ">" or character == "<" or character == "=" or character == "!":
            buff = character
            character = self.source.get_next_char()
            if (buff + character) in Symbol.double_operators:
                token_type = Symbol.double_operators[buff + character]
                self.token = Token(token_type, buff + character)
                self.source.get_next_char()
                return True
            elif buff in Symbol.special_characters:
                token_type = Symbol.special_characters[buff]
                self.token = Token(token_type, buff)
                return True
        return False


    def try_identifier(self):
        word = self.read_identifier()
        if word in Symbol.key_words:
            token_type = Symbol.key_words[word]
            self.token = Token(token_type, word)
            return True
        elif word != "":
            self.token = Token(Type.IDENTIFIER, word)
            return True
        return False


    def try_single_character(self):
        character = self.source.get_char()
        if character in Symbol.special_characters:
            token_type = Symbol.special_characters[character]
            self.token = Token(token_type, character)
            self.source.get_next_char()
            return True
        return False
