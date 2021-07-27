from batch import Batch
from run import Run
from command_handler import CommandHandler
from database import DataBase


class CLI:

    def __init__(self):
        self._data_base = DataBase()
        self._commands = CommandHandler()

    def run(self):
        while True:
            try:
                if not Batch.batch_mode:
                    command = input("> cmd >>> ")
                else:
                    command = input("> batch >>> ")
                command_list = self.create_command_parts_list(command)
                if command_list[0].lower() == "batch":
                    if not Batch.batch_mode:
                        Batch.batch_name = " ".join(command_list[1:])
                        self._data_base.add_batch(Batch.batch_name)
                        Batch.batch_mode = True
                    else:
                        raise Exception("allready in batch mode")
                elif command_list[0].lower() == "run":
                    if Batch.batch_mode:
                        raise Exception("can't run batch_package during batch mode")
                    else:
                        Run().execute(command_list[1:])
                else:
                    self._commands.handler(command_list)
            except Exception as e:
                print(e)

    def create_command_parts_list(self, command):
        command = " ".join(command.split())
        command_list = command.split(' ')
        return command_list
