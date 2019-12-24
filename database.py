import datetime


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.hist = None
        self.load()

    def load(self):
        self.file = open(self.filename, "a+")
        self.hist = {}

        for lines in self.file:
            types, quant = lines.strip().split(";")
            self.hist[types] = quant

        self.file.close()

    def add_entry(self, types, quant):
        updated = 0
        f = open(self.filename,  "r+")
        fff = open("temp.txt", "w+")

        content = f.readlines()

        for aline in content:
            lines = aline.strip().split(";")
            if lines[0] == types:
                updated = 1
                new_str = "".join(lines[0] + ";" + quant + "\n")
                fff.write(new_str)
            else:

                fff.write(aline)
        if updated == 0:
            fff.write(types + ";" + quant + "\n")

        fff.close()
        fff = open("temp.txt", "r+")

        data = fff.readlines()

        f.close()
        f = open(self.filename, "r+")
        f.truncate(0)
        f.close()

        f = open(self.filename, "r+")

        for every in data:
            if every not in f:
                f.write(every)

        f.close()


        fff.close()

    def get_entry(self, types):
        fd = open("history.txt", "r")
        contents = fd.readlines()
        fd.close()

        for lin in contents:
            line = lin.split(";")
            if line[0] == types:
                fin = line[1].split("\n")
                return fin[0]

        return -1

