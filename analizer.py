from database import DataBase
from analizer_package import FindAll, Len, Find, Count



class Analizer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Analizer.__instance:
            Analizer.__instance = object.__new__(cls)
        return Analizer.__instance

    def __init__(self, type):
        self.seq_database = DataBase()
        super().__init__()
        self._analizer_types = {
            "len": Len,
            "find": Find,
            "count": Count,
            "findall": FindAll
        }
        self._type = type.lower()

    def executor(self, command_list):
        seq_name, sequence = self.initialization(command_list)
        if len(command_list) == 0:
            raise Exception("command {} has to get arguments".format(self._type))
        if len(command_list) > 1 and command_list[1][0] == '#':
            command_list[1] = DataBase.get_sequence_by_id(int(command_list[1][1:])).get_sequence()
        ret_val = self._analizer_types[self._type]().execute(command_list[1:], sequence)
        print("{}".format(ret_val))

    def initialization(self, command_list):
        # if there is id
        if command_list[0][0] == '#':
            seq_name = DataBase.get_seq_name_by_id(int(command_list[0][1:]))
            sequence = DataBase.get_sequence_by_id(int(command_list[0][1:]))
        elif command_list[0][0] == '@':
            seq_name = command_list[0][1:]
            sequence = DataBase.get_sequence_by_name(command_list[0][1:])
        # there is no id or name
        else:
            raise Exception("{} command has to get id prefixed by # or name prefixed by @".format(self._type))
        return seq_name, sequence
