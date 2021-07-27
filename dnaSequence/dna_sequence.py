# represents a dna sequence
import re


class DnaSequence:
    def __init__(self, sequence):
        if self.is_valid(sequence):
            self._sequence = sequence
            self._counter = 1
        else:
            raise ValueError("sequence can only have letters: A,C,G,T")

    def get_counter(self):
        return self._counter

    def set_counter(self, counter):
        self._counter = counter

    def is_valid(self, sequence):
        pattern = re.compile('[^A,C,G,T]')
        if pattern.findall(sequence):
            return False
        return True

    def insert(self, nucleotide, index):
        if not self.is_valid(nucleotide):
            raise ValueError
        if index > len(self._sequence):
            raise IndexError
        if not isinstance(index, int):
            raise TypeError
        temp1 = self._sequence[:index]
        temp2 = self._sequence[index:]
        self._sequence = temp1 + nucleotide + temp2

    def get_sequence(self):
        return self._sequence

    def assignment(self, other):
        if isinstance(other, str):
            if not self.is_valid(other):
                raise ValueError("sequence can only have letters: A,C,G,T")
            else:
                self._sequence = other
        elif isinstance(other, DnaSequence):
            if not self.is_valid(other.get_sequence()):
                raise ValueError("sequence can only have letters: A,C,G,T")
            else:
                self._sequence = other.get_sequence()
        else:
            raise ValueError
        return self

    def __str__(self):
        return "{}".format(self._sequence)

    def __eq__(self, other):
        return self._sequence == other.get_sequence()

    def __ne__(self, other):
        return ~self.__eq__(other)

    def __setitem__(self, index, char):
        if int(index) > len(self._sequence):
            raise IndexError("not a valid command. please try again.")
        self._sequence = self._sequence[:index] + char + self._sequence[index + 1:]

    def __getitem__(self, index):
        if int(index) > len(self._sequence):
            raise IndexError
        return self._sequence[int(index)]

    def __len__(self):
        return len(self._sequence)
