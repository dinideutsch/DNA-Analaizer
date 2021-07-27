from database import DataBase


class Save:
    def execute(self,command_list, seq_name, sequence ):
        # seq_name, sequence = self.initialization(command_list)
        if len(command_list) > 1 and command_list[-1][-7:] == '.rawdna':
            file_name = "".join(command_list[1:])
        elif len(command_list) == 1:
            file_name = seq_name + ".rawdna"
        else:
            raise Exception("suffix of filename must be .rawdna")
        with open(file_name, 'w')as f:
            f.write(sequence.get_sequence())
        print("[{}] {} saved successfully".format(DataBase.get_seq_id_by_name(seq_name), seq_name))



