import os


class FilesystemHandler:
    def __init__(self):
        pass

    def read_from_file(self, filename):
        if not os.path.exists("filename"):
            raise Exception("Bad filename")
        infile = open(filename, "r")
        line = infile.readline()
        return line
