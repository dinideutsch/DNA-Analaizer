import re


class Count:
    def execute(self, command_list, sequence):
        if len(command_list) < 1:
            raise Exception("count command has to get tow arguments")
        ret_arr = []
        for i in range(len(sequence.get_sequence())):
            ret_arr += [m.start() + i for m in re.finditer(command_list[0], sequence.get_sequence()[i:])]
        ret_arr = set(ret_arr)
        return len(ret_arr)