class FilesystemHandler:
    def __init__(self):
        pass

    def read_from_file(self, filename):
        infile = open(filename, "r")
        line = infile.readline()
        return line
