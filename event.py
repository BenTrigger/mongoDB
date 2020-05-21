import datetime


class Event:
    count = 1
    def __init__(self):
        self.date = datetime.datetime.now()
        self.name = 'class insert' + str(Event.count)
        self.files = []
        Event.count += 1
        self.bin_files = []

    def set__file_path(self, path="../out/", file_name="empty"):
        self.files.append(path + file_name)
        return self

    def add_bin_file(self, byteArr):
        self.bin_files.append(byteArr)
        return self

    # def inser_bin_file(self, binFile):
    #     self.bin_files.append(binFile)
    #     return self