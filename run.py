from command_handler import CommandHandler
from database import DataBase


class Run:
    def __init__(self):
        self._data_base = DataBase()
        self._command_handler = CommandHandler()

    def execute(self, command_list):
        if len(command_list) == 0:
            raise Exception("command run has to get batch_package name")
        if command_list[0][0] != '@':
            raise Exception("batch_package name has to begin with @")
        command_list[0] = command_list[0][1:]
        name = " ".join(command_list)
        batch = self._data_base.get_batch(name)
        for i in batch:
            CommandHandler().handler(i)
