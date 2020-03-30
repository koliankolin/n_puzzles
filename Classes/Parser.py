import atexit
import os

EXIT = False

class Parser:
    def __init__(self, file_name=None):
        self.data = []
        self.dim = None
        if file_name:
            if not os.path.isfile(file_name):
                raise ValueError('No such file')
            with open(file_name, 'r') as f:
                for line in f:
                    line = line.strip()
                    if '#' in line:
                        line = line.split('#')[0].strip()
                        if not line:
                            continue
                    line = list(filter(lambda x: x, line.split(' ')))
                    if sum([not char.isnumeric() for char in line]) > 0:
                        continue
                    if len(line) == 1 and line[0].isnumeric():
                        self.dim = int(line[0])
                        continue
                    self.data.append(line)
                self.data = list(filter(lambda x: x, self.data))
            if not self.dim:
                raise ValueError('There is no definition of dimensionality')
            if len(self.data) != self.dim:
                raise ValueError('It is not quadratic :((')
            if sum([len(i) != self.dim for i in self.data]) > 0:
                raise ValueError('Dimensionality of line is not stable')
        else:
            while not EXIT:
                try:
                    line = input().strip()
                    if '#' in line:
                        line = line.split('#')[0].strip()
                        if not line:
                            continue
                    line = line.split(' ')
                    if sum([not char.isnumeric() for char in line]) > 0:
                        continue
                    self.data.append(line)
                except EOFError:
                    self.dim = len(self.data)
                    if sum([len(i) != self.dim for i in self.data]) > 0:
                        raise ValueError('Dimensionality of line is not stable')
                    break
        if sum([int(j) for i in self.data for j in i]) != sum(range(self.dim ** 2)):
            raise ValueError('Duplicate numbers in input ;)')

    def get_data(self):
        return self.data

def quit():
    global EXIT
    print('Thanks for everything!')
    EXIT = True

atexit.register(quit)


