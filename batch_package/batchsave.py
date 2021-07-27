
from database import DataBase


class BatchSave:
    def __init__(self):
        self._batches = DataBase()

    def execute(self, command_list):
        if len(command_list) > 1 and command_list[1][-command_list[1][::-1].index('.')-1:] == '.dnabatch':
            file_name = "".join(command_list[1:])
        elif len(command_list) == 1:
            file_name = command_list[0][1:] + ".dnabatch"
        else:
            raise Exception("suffix of filename must be .rawdna")
        if command_list[0][0] != '@':
            raise Exception("a batch_package name has to begin with @")
        with open(file_name, 'w')as f:
            print(self._batches.get_batch(command_list[0][1:]))
            for i in self._batches.get_batch(command_list[0][1:]):
                   f.write(" ".join(i) + '\n')
        print("{} saved successfully in {}".format(command_list[0][1:], file_name))
