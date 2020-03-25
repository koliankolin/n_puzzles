class Node:
    def __init__(self, puzzle_data, g_score=0, metric='euclead'):
        self.puzzle_data = puzzle_data
        self.dim = len(puzzle_data)
        self.puzzle_goal = self._generate_puzzle_goal()
        self.coords_empty_block = self._find_coords_empty_block()
        self.g_score = g_score
        self.metric = metric
        self.f_score = self.get_f_score()

    def get_h_score(self):
        if self.metric == 'simple':
            return self._get_h_simple()
        if self.metric == 'manhetten':
            return self._get_h_manhatten()
        if self.metric == 'euclead':
            return self._get_h_euclead()

    def _get_h_simple(self):
        result = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.puzzle_data[i][j] != self.puzzle_goal[i][j]:
                    result += 1
        return result

    def _get_h_manhatten(self):
        result = 0
        for i in range(self.dim):
            for j in range(self.dim):
                result += abs(int(self.puzzle_data[i][j]) - int(self.puzzle_goal[i][j]))
        return result

    def _get_h_euclead(self):
        result = 0
        for i in range(self.dim):
            for j in range(self.dim):
                result += (int(self.puzzle_data[i][j]) - int(self.puzzle_goal[i][j])) ** 2
        return result

    def get_f_score(self):
        return self.get_h_score() + self.g_score

    def _find_coords_empty_block(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.puzzle_data[i][j] == 0 or self.puzzle_data[i][j] == '0':
                    return i, j
        return None

    def _right(self):
        if self._check_possible_move('right'):
            return [self.coords_empty_block[0], self.coords_empty_block[1] + 1]
        return False

    def _left(self):
        if self._check_possible_move('left'):
            return [self.coords_empty_block[0], self.coords_empty_block[1] - 1]
        return False

    def _top(self):
        if self._check_possible_move('top'):
            return [self.coords_empty_block[0] - 1, self.coords_empty_block[1]]
        return False

    def _bottom(self):
        if self._check_possible_move('bottom'):
            return [self.coords_empty_block[0] + 1, self.coords_empty_block[1]]
        return False

    def _change_coords_empty_block(self, new_coords):
        if new_coords[0] < 0 or new_coords[0] > self.dim or new_coords[1] < 0 or new_coords[1] > self.dim:
            raise ValueError(f'New coords are incorrect {new_coords}')
        temp_puzzle = [i.copy() for i in self.puzzle_data]
        temp_val = temp_puzzle[new_coords[0]][new_coords[1]]
        temp_puzzle[new_coords[0]][new_coords[1]] = \
            self.puzzle_data[self.coords_empty_block[0]][self.coords_empty_block[1]]
        temp_puzzle[self.coords_empty_block[0]][self.coords_empty_block[1]] = temp_val
        return temp_puzzle

    def _check_possible_move(self, direction):
        if direction == 'top':
            return self.coords_empty_block[0] - 1 >= 0
        elif direction == 'bottom':
            return self.coords_empty_block[0] + 1 < self.dim
        elif direction == 'right':
            return self.coords_empty_block[1] + 1 < self.dim
        elif direction == 'left':
            return self.coords_empty_block[1] - 1 >= 0
        else:
            raise ValueError('No such direction to move')

    def find_other_coords(self):
        nodes = []
        for find_direction in [self._top, self._bottom, self._right, self._left]:
            coord = find_direction()
            if coord:
                nodes.append(Node(self._change_coords_empty_block(coord), self.g_score + 1, self.metric))
        return nodes

    def _generate_puzzle_goal(self):
        temp = []
        result = []
        for i in range(1, self.dim ** 2 + 1):
            temp.append(str(i))
            if len(temp) % self.dim == 0:
                result.append(temp)
                temp = []
        result[self.dim - 1][self.dim - 1] = '0'
        return result

    def _is_sovable(self):
        pass

    def visualize_current_state(self):
        for i in range(self.dim):
            print(' '.join(self.puzzle_data[i]))

data = '''2 4 3
0 5 6
7 8 1'''.split('\n')
data = [i.split(' ') for i in data]

node = Node(puzzle_data=data, g_score=0)
node.visualize_current_state()
print()
for i in node.find_other_coords():
    i.visualize_current_state()
    print(i.get_h_score())
    print()
