import datetime
import os


class Database1:
    def __init__(self, filename):
        self.filename = filename
        self.trans = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "a+")
        self.trans = {}

        for lines in self.file:
            date, quant, types, price, total = lines.strip().split(";")
            self.trans[date] = total

        self.file.close()

    def add_entry(self, types, quant, price):
        date = str(datetime.datetime.now()).split(" ")[0]
        total = int(price)*(int(quant))

        fd = open(self.filename, "a")

        fd.write(date + ";" + str(quant) + ";" + str(types) + ";" + str(price) + ";" + str(total) + "\n")

        fd.close()

    def clear_entries(self):
        ffd = open(self.filename, "w")
        ffd.close()

    def get_entry(self, date):
        if date in self.trans:
            return self.trans[date]
        else:
            return -1
