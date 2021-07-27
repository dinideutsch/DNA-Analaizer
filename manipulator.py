from database import DataBase
from manipulator_package import Pair, Replace


class Manipulator:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Manipulator.__instance:
            Manipulator.__instance = object.__new__(cls)
        return Manipulator.__instance

    def __init__(self, type):
        self.seq_database = DataBase()
        super().__init__()
        self._manipulator_types = {
            "pair": Pair,
            "replace": Replace,
        }
        self._type = type.lower()

    def executor(self, command_list):
        # Validations & Initializations
        seq_name, sequence = self.initialization(command_list)
        # create new?
        try:
            dup_flag = command_list.index(':')
        except:
            dup_flag = len(command_list)
        if dup_flag == len(command_list):
            name = seq_name
        else:
            # Creating the name:
            name = self.create_name(command_list[dup_flag + 1:], seq_name)
        # Manipulating
        return_sequence = self._manipulator_types[self._type]().execute(sequence, command_list[1:dup_flag])
        self.seq_database.add_dna_sequence({name: return_sequence})
        # Print message
        self.print_message(return_sequence, name)

    def print_message(self, return_sequence, name):
        if len(return_sequence.get_sequence()) > 40:
            seq = return_sequence.get_sequence()[:32] + "..." + return_sequence.get_sequence()[-3:]
        else:
            seq = return_sequence.get_sequence()
        print("[{}] {}: {}".format(self.seq_database.get_seq_id_by_name(name), name, seq))

    def create_name(self, name_list, seq_name):
        name = ""
        # create default name
        if len(name_list) == 0 or len(name_list) == 1 and name_list[0] == '@@':
            counter = self.seq_database.get_sequence_by_name(seq_name).get_counter()
            name = seq_name + "_" + self._type[0] + str(counter)
            self.seq_database.get_sequence_by_name(seq_name).set_counter(counter + 1)
        else:
            name_list[0] = name_list[0][1:]
            for i in name_list:
                name += (str(i) + " ")
            name = name[:-1]
        return name

    def initialization(self, command_list):
        # if there is no arguments
        if len(command_list) == 0:
            raise Exception("command {} has to get arguments".format(self._type))
        # if there is id
        if command_list[0][0] == '#':
            seq_name = self.seq_database.get_seq_name_by_id(self.seq_database, int(command_list[0][1:]))
            # sequence is the manipulated dna_seq
            sequence = self.seq_database.get_sequence_by_id(int(command_list[0][1:]))
        elif command_list[0][0] == '@':
            seq_name = command_list[0][1:]
            sequence = self.seq_database.get_sequence_by_name(command_list[0][1:])
        # there is no id or name
        else:
            raise Exception("{} command has to get id prefixed by # or name prefixed by @".format(self._type))
        return seq_name, sequence
