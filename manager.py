from database import DataBase
from manager_package import Delete, Save


class Manager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Manager.__instance:
            Manager.__instance = object.__new__(cls)
        return Manager.__instance

    def __init__(self, type):
        self.seq_database = DataBase()
        super().__init__()
        self._manager_types = {
            "save": Save,
            "del": Delete
        }
        self._type = type.lower()

    def executor(self, command_list):
        seq_name, sequence = self.initialization(command_list)
        if len(command_list) == 0:
            raise Exception("command {} has to get arguments".format(self._type))
        self._manager_types[self._type]().execute(command_list, seq_name, sequence)

    def initialization(self, command_list):
        # if there is id
        if len(command_list) == 0:
            raise Exception("command has to get arguments")
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
