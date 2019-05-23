# source.py
# zalozenie: przy inicjacji Source znak ustawiany jest na pierwszy
# znak w strumieniu danych
import sys

class Source:
    def __init__(self, source_stream):
        self.line_number = 1
        self.column = 0
        self.source_stream = source_stream
        self.character = self.get_next_char()

    def get_char(self):
        return self.character

    def get_position(self):
        return self.line_number, self.column

    def get_next_char(self):
        self.character = self.source_stream.read(1)
        if self.character == '#':
            while self.character != '\n' and self.character != '':
                self.character = self.source_stream.read(1)
        if self.character == '\n':
            self.line_number += 1
            self.column = 0
        else:
            self.column += 1
        return self.character

    def print_line(self, line_number):
        pos = self.source_stream.tell()
        self.source_stream.seek(0)

        for i in range(0, line_number - 1):
            self.source_stream.readline()
        print(self.source_stream.readline())

        self.source_stream.seek(pos)
        return self.source_stream