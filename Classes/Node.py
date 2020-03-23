class Node:
    def __init__(self, puzzle_data, puzzle_goal, g_score, metric='simple'):
        self.puzzle_data = puzzle_data
        self.puzzle_goal = puzzle_goal
        self.dim = len(puzzle_data)
        self.coords_empty_block = self._find_coords_empty_block()
        self.g_score = g_score
        self.metric = metric

    def get_h_score(self):
        if self.metric == 'simple':
            return self._get_h_simple()

    def _get_h_simple(self):
        result = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.puzzle_data[i][j] != self.puzzle_goal[i][j]:
                    result += 1
        return result

    def get_f_score(self):
        return self.get_h_score() + self.g_score

    def find_other_states(self):
        pass

    def _find_coords_empty_block(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.puzzle_data[i][j] == 0:
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
            return [self.coords_empty_block[0] + 1, self.coords_empty_block[1]]
        return False

    def _bottom(self):
        if self._check_possible_move('bottom'):
            return [self.coords_empty_block[0] - 1, self.coords_empty_block[1]]
        return False

    def _change_coords_empty_block(self, new_coords):
        if new_coords[0] < 0 or new_coords[0] > self.dim or new_coords[1] < 0 or new_coords[1] > self.dim:
            raise ValueError('New coords are incorrect')
        temp_puzzle = self.puzzle_data[:]
        temp_puzzle[new_coords[0], new_coords[1]] = self.puzzle_data[self.coords_empty_block[0], self.coords_empty_block[1]]
        return temp_puzzle

    def _check_possible_move(self, direction):
        if direction == 'top':
            return self.coords_empty_block[0] + 1 <= self.dim
        elif direction == 'bottom':
            return self.coords_empty_block[0] - 1 >= self.dim
        elif direction == 'right':
            return self.coords_empty_block[1] + 1 <= self.dim
        elif direction == 'left':
            return self.coords_empty_block[1] - 1 >= self.dim
        else:
            raise ValueError('No such direction to move')

    def _find_other_coords(self):
        nodes = []
        for find_direction in [self._top, self._bottom, self._right, self._left]:
            coord = find_direction(self)
            if coord:
                nodes.append(Node(self._change_coords_empty_block(coord), self.g_score + 1, self.puzzle_goal))
                return nodes.sort(key=lambda x: x.f_score, reverse=False)

    def _make_step(self, direction):
        if direction == 'top':
            self.puzzle_data = self._change_coords_empty_block(self._top())
        elif direction == 'bottom':
            self.puzzle_data = self._change_coords_empty_block(self._bottom())
        elif direction == 'right':
            self.puzzle_data = self._change_coords_empty_block(self._right())
        elif direction == 'left':
            self.puzzle_data = self._change_coords_empty_block(self._left())
        else:
            raise ValueError(f'Can not possible to make step in {direction}')
