from batch_package import BatchList, BatchLoad, BatchSave, BatchShow
from database import DataBase


class Batch:
    __instance = None
    batch_name = ""
    batch_mode = False

    def __new__(cls, *args, **kwargs):
        if not Batch.__instance:
            Batch.__instance = object.__new__(cls)
        return Batch.__instance

    def __init__(self, type):
        super().__init__()
        self._batch_types = {
            "batchload": BatchLoad,
            "batchsave": BatchSave,
            "batchlist": BatchList,
            "batchshow": BatchShow,
        }
        self._data_base = DataBase()
        self._type = type.lower()

    def executor(self, command_list):
        self._batch_types[self._type]().execute(command_list)
