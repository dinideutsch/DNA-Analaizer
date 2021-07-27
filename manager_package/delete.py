from database import DataBase


class Delete:
    def __init__(self):
        self.dna_collection = DataBase

    def execute(self, command_list, seq_name, sequence):
        #     seq_name, sequence = self.initialization(command_list)
        print("Do you really want to delete {} : {}?".format(seq_name, sequence.get_sequence()))
        while True:
            print("Please confirm by 'y' or 'Y' , or cancel by 'n' or 'N' .")
            confirm = input("> confirm >>> ")
            if confirm.lower() == "y":
                id = self.dna_collection.get_seq_id_by_name(seq_name)
                self.dna_collection.delete_from_data_base(seq_name)
                print("Deleted: [{}] {} {}".format(id, seq_name,
                                                   sequence.get_sequence()))
                break
            elif confirm.lower() == "n":
                print("Canceled deletion")
                break
            else:
                print("You have typed an invalid response. Please either confirm by 'y' / 'Y' , orcancel by 'n' / 'N' .")

