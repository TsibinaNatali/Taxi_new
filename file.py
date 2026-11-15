from Taxi import *
class File:
    def __init__(self, filename):
        self.filename = filename

    def get_lines(self):
        with open(self.filename, 'r', encoding="UTF-8") as file:
            ls = list()
            for i in file.readlines():
                ls.append(i)
            return ls
    def save_lines(self,lines:list[str]):
        with open(self.filename, 'w', encoding="UTF-8") as file:
            file.writelines(lines)