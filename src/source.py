# source.py
# zalozenie: przy inicjacji Source znak ustawiany jest na pierwszy
# znak w strumieniu danych
import sys


class Source:
    def __init__(self):
        self.line_number = 1
        self.position = 0
        self.character = self.get_next_char()


    def get_char(self):
        return self.character


    def get_position(self):
        return self.line_number, self.position


    def get_next_char(self):
        self.character = sys.stdin.read(1)
        if self.character == '#':
            while self.character != '\n' and self.character != '':
                self.character = sys.stdin.read(1)
        if self.character == '\n':
            self.line_number += 1
            self.position = 0
        else:
            self.position += 1
        return self.character
