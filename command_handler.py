from batch import Batch
from creator import Creator
from database import DataBase
from manager import Manager
from manipulator import Manipulator
from analizer import Analizer


class CommandHandler:
    def __init__(self):
        self._command_types = {
            "new": Creator,
            "load": Creator,
            "dup": Creator,
            "pair": Manipulator,
            "replace": Manipulator,
            "save": Manager,
            "del": Manager,
            "len": Analizer,
            "find": Analizer,
            "count": Analizer,
            "findall": Analizer,
            "batch": Batch,
            "batchload": Batch,
            "batchsave": Batch,
            "batchlist": Batch,
            "batchshow": Batch,
            "end": Batch
        }
        self._data_base = DataBase()

    def handler(self, command_list):
        if command_list[0].lower() == "end":
            Batch.batch_mode = False
        else:
            if Batch.batch_mode:
                if command_list[0].lower().find("batch") == -1:
                    self._data_base.add_to_batch(Batch.batch_name, command_list)
                    return
            try:
                reciever = self._command_types[command_list[0].lower()]
            except:
                raise KeyError("not a valid command. please try again")
            reciever(command_list[0].lower()).executor(command_list[1:])
