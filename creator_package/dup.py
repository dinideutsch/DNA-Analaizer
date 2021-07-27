from database import DataBase
from dnaSequence import DnaSequence


class Dup:
    def __init__(self):
        pass

    def execute(self, command):
        if command[0][0] != "#":
            raise SystemError("id must with #")
        sequence = DataBase.get_sequence_by_id(int(command[0][1:]))
        if len(command) == 1 or (len(command) == 2 and command[1] == '@'):
            name = DataBase.get_seq_name_by_id(int(command[0][1:]))+"_"+str(sequence.get_counter())
            sequence.set_counter(sequence.get_counter()+1)
        elif len(command) > 1:
            if command[1][0] != '@':
                raise ValueError("sequence name has to begin with a @")
            name = command[1][1:]
            for i in command[1][1:]:
                name = name + str(i)
        else:
            raise IndexError("command new has to get an id")
        return {name: DnaSequence(sequence.get_sequence())}
