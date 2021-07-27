class DataBase:
    dna_collection = {}
    batch_collection = {}
    counter = 1

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DataBase.__instance:
            DataBase.__instance = object.__new__(cls)
        return DataBase.__instance

    def add_batch(self, name):
        if not name:
            raise Exception("batch has to get a name")
        DataBase.batch_collection.update({name: []})

    def load_batch(self, name, batch):
        DataBase.batch_collection.update({name: batch})

    def get_batch(self, name):
        try:
            return DataBase.batch_collection[name]
        except KeyError:
            raise Exception("no such a key in batch_package collection")

    def get_batches(self):
        return DataBase.batch_collection

    def add_to_batch(self, name, command):
        DataBase.batch_collection[name].append(command)

    @staticmethod
    def delete_from_data_base(key):
        del DataBase.dna_collection[key]
        DataBase.counter -= 1

    @staticmethod
    def add_dna_sequence(value):
        DataBase.dna_collection.update(value)
        DataBase.counter += 1

    @staticmethod
    def get_sequence_by_name(name):
        try:
            return DataBase.dna_collection[name]
        except KeyError:
            raise Exception("no such a key in DNA collection")

    @staticmethod
    def get_seq_name_by_id(id):
        return list(DataBase.dna_collection.keys())[id - 1]

    @staticmethod
    def get_sequence_by_id(id):
        return list(DataBase.dna_collection.values())[id - 1]

    @staticmethod
    def get_seq_id_by_name(name):
        return list(DataBase.dna_collection.keys()).index(name) + 1
