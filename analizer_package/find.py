class Find:
    def execute(self, command_list, sequence):
        if len(command_list) > 1:
            raise Exception("too many arguments for command find")

        ret_val = sequence.get_sequence().find(command_list[0])+1
        return ret_val if ret_val > 0 else None
