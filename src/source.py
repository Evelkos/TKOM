# source.py

class Source:
    def __init__(self, filename):
        self.count = 0
        self.filename = filename
        self.file = open(self.filename, "r")
        print("Open")


    def __del__(self):
        self.file.close
        print("Closed")

    def read_char(self):
        return self.file.read(1)
