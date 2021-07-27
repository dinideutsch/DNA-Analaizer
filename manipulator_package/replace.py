class Replace:
    def execute(self, sequence, command):
        if len(command) % 2 == 1:
            raise Exception("each id must have a value")
        is_odd = True
        for i in command:
            if is_odd:
                sequence[int(i)] = command[command.index(i) + 1]
            if is_odd:
                is_odd = False
            else:
                is_odd = True
        return sequence
