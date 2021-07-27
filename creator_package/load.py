from database import DataBase
from dnaSequence import DnaSequence


class Load:

    def __init__(self):
        pass

    def execute(self, command):
        split_values = self.split_command(command)
        sequence = self.read_rawdna(split_values[0])
        name = command[split_values[1] + 1:]
        if len(name) >= 1:
            if name[0][0] != '@':
                raise ValueError("sequence name has to begin with a @")
            name[0] = name[0][1:]
        elif len(name) == 0 or (len(name) == 1 and name[0] == '@'):
            name = split_values[0][:-7] + "_" + str(DataBase.counter)
        else:
            raise IndexError("command load has to get a sequence string")
        return {"".join(name): DnaSequence(sequence)}

    def read_rawdna(self, file_name):
        with open(file_name, 'r') as file:
            sequence = file.read().splitlines()
        return "".join(sequence)

    def split_command(self, command_list):
        file_name = ""
        for i in command_list:
            file_name = file_name + i
            if i.find(".rawdna"):
                return file_name, command_list.index(i)
        raise FileNotFoundError("file name must be followed with .rawdna suffix")
