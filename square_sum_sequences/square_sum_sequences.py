import math


class NaiveSquareSumSequence():

    def __init__(self, seed, length):
        self.sequence = [seed]
        for _ in xrange(length - 1):
            self.append_next_value()

    def append_next_value(self):
        self.sequence.append(self.next_value())

    @staticmethod
    def is_square(value):
        return round(math.sqrt(value)) ** 2 == value

    def next_value(self):
        delta = 1
        while True:
            if NaiveSquareSumSequence.is_square(self.sequence[-1] + delta) and delta not in self.sequence:
                return delta
            delta += 1

    def to_list(self):
        return self.sequence


class FastSquareSumSequence():

    def __init__(self, seed, length):
        self.mapping = {0: seed}
        self.last_value = seed
        for _ in xrange(length + 1):
            self.append_next_value()

    def append_next_value(self):
        self.mapping[self.last_value] = self.next_value()
        self.last_value = self.mapping[self.last_value]

    def next_value(self):
        root = int(math.ceil(math.sqrt(self.last_value)))
        delta = root ** 2 - self.last_value
        while delta == 0 or delta in self.mapping:
            delta += 2 * root + 1
            root += 1
        return delta

    def to_list(self):
        sequence = [self.mapping[0]]
        while sequence[-1] in self.mapping:
            sequence.append(self.mapping[sequence[-1]])
        return sequence
