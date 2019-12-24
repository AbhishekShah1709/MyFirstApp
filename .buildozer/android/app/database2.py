class Database2:
    def __init__(self, filename):
        self.filename = filename

    def add_entry(self, new_amount):
        fd1 = open(self.filename, "w+")
        fd1.write(str(new_amount))
        fd1.close()

    def get_entry(self):
        fd2 = open(self.filename, "a+")
        fd2.seek(0,0)
        data = fd2.readlines()
        fd2.close()
        for content in data:
            contents = content.strip()
            return contents
