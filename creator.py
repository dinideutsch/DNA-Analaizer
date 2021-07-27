from database.data_base import DataBase
from creator_package import Dup, Load,  New


class Creator:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Creator.__instance:
            Creator.__instance = object.__new__(cls)
        return Creator.__instance

    def __init__(self, type):
        self.seq_database = DataBase()
        self._creator_types = {
            "new": New,
            "load": Load,
            "dup": Dup
        }
        self._type = type.lower()

    def executor(self, command_list):
        if len(command_list) == 0:
            raise Exception("command {} has to get arguments".format(self._type))
        return_sequence = self._creator_types[self._type]().execute(command_list)
        self.seq_database.add_dna_sequence(return_sequence)
        key = list(return_sequence.keys())[0]
        if len(return_sequence[key].get_sequence()) > 40:
            seq = return_sequence[key].get_sequence()[:32] + "..." + return_sequence[key].get_sequence()[-3:]
        else:
            seq = return_sequence[key].get_sequence()
        print("[{}] {}: {}".format(self.seq_database.counter - 1, key, seq))
