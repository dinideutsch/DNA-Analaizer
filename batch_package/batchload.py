from database import DataBase


class BatchLoad:
    def __init__(self):
        self._database = DataBase()

    def execute(self, command_list):
        batch = self.read_dnabatch(command_list[0])
        name = command_list[1:]
        if len(name) == 2:
            if name[1][0] != '@':
                raise ValueError("sequence name has to begin with a @")
            name = name[1][1:]
        elif len(name) == 0:
            index = -command_list[0][::-1].index('.')
            name = command_list[0][:index-1]
        else:
            raise IndexError("command batchload can get: filename + : + default name only")
        self._database.load_batch(name, batch)
        print("loaded batch_package {} succefully".format(name))

    def read_dnabatch(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        batch = []
        for line in lines:
            batch.append(line[:-1].split(" "))
        return batch

