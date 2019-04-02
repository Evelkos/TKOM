# source.py

import os


class Source:
    def __init__(self, filename):
        self.line_number = 1
        self.position = 0
        self.file = open(filename, "r")
        self.character = ''
        print("Open")


    def __del__(self):
        self.file.close()
        print("Closed")


    def get_char(self):
        return self.character


    def get_line_number(self):
        return self.line_number


    def get_position(self):
        return self.position


    def get_next_char(self):
        self.character = self.file.read(1)
        if self.character == '\n':
            self.line_number += 1
            self.position = 0
        else:
            self.position += 1
        return self.character

    def undo_get_next_char(self):
        self.counter = self.counter - 1
        self.file.seek(self.counter, 0)

# source = Source("../test/test.txt")
# print(source.get_next_char())
# print(source.get_next_char())
# print(source.get_next_char())
# print(source.get_next_char())