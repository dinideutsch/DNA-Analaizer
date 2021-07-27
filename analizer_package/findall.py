import re


class FindAll:
    def execute(self, command_list, sequence):
        ret_arr = []
        for i in range(len(sequence.get_sequence())):
            ret_arr += [m.start()+i for m in re.finditer(command_list[0], sequence.get_sequence()[i:])]
        ret_val = " "
        if not ret_arr:
            return None
        ret_arr = set(ret_arr)
        for i in ret_arr:
            ret_val += str(i + 1) + " "
        return ret_val
