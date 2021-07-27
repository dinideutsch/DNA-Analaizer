from database import DataBase


class BatchList:
    def __init__(self):
        self._batches = DataBase().get_batches()

    def execute(self, command_list):
        for i in list(self._batches.keys()):
            print(i)
