from database import DataBase


class BatchShow:
    def __init__(self):
        self._batches = DataBase()

    def execute(self, command_list):
        if len(command_list) < 1:
            raise Exception("command Show has get a batch_package name")
        if command_list[0][0] != '@':
            raise Exception("a batch_package name has to begin with @")
        command_list[0] = command_list[0][1:]
        name = " ".join(command_list)
        batch_list = self._batches.get_batch(name)
        for i in batch_list:
            print(i)
