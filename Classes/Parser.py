import atexit
import os

EXIT = False

class Parser:
    def __init__(self, file_name=None):
        self.data = []
        if file_name:
            if not os.path.isfile(file_name):
                raise ValueError('No such file')
            with open(file_name, 'r') as f:
                dim = None
                for line in f:
                    line = line.strip().split(' ')
                    if sum([i not in '1234567890' for i in line]) > 0:
                        continue
                        # raise ValueError(f'Invalid input in line {line}')
                    if len(line) == 1:
                        dim = int(line[0])
                        continue
                    self.data.append(line)
            if not dim:
                raise ValueError('There is no definition of dimensionality')
            if len(self.data) != dim:
                raise ValueError('It is not quadratic :((')
            if sum([len(i) != dim for i in self.data]) > 0:
                raise ValueError('Dimensionality of line is not stable')
        else:
            while not EXIT:
                try:
                    row = input().strip().split(' ')
                    if sum([i not in '1234567890' for i in row]) > 0:
                        continue
                        # raise ValueError(f'Invalid input in line {row}')
                    self.data.append(row)
                except EOFError:
                    dim = len(self.data)
                    if sum([len(i) != dim for i in self.data]) > 0:
                        raise ValueError('Dimensionality of line is not stable')
                    break
        if sum([int(j) for i in self.data for j in i]) != sum(range(dim ** 2)):
            raise ValueError('Duplicate numbers in input ;)')

    def get_data(self):
        return self.data


def quit():
    global EXIT
    print('Thanks for everything!')
    EXIT = True

atexit.register(quit)


