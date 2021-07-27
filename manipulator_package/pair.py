class Pair:
    def execute(self, sequence, command_list):
        if len(command_list) > 0:
            raise Exception("too many arguments for command pair")
        for i in range(len(sequence)):
            if sequence[i] == 'A':
                sequence[i] = 'T'
            elif sequence[i] == 'T':
                sequence[i] = 'A'
            elif sequence[i] == 'C':
                sequence[i] = 'G'
            elif sequence[i] == 'G':
                sequence[i] = 'C'
        return sequence
