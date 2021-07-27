from database import DataBase
from dnaSequence import DnaSequence


class New:
    def __init__(self):
        pass

    def execute(self, command):
        name = command[1:]
        if len(name) > 0 and len(name[0]) >= 1:
            if name[0][0] != '@':
                raise ValueError("sequence name has to begin with a @")
            name[0] = name[0][1:]
        elif len(name) == 0 or (len(name) == 1 and name[0] == '@'):
            name.append("seq_" + str(DataBase.counter))
        else:
            raise IndexError("command new has to get a sequence string")
        return {"".join(name): DnaSequence(command[0])}
