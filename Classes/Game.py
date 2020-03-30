from Classes.Node import Node

class Game:
    def __init__(self, start_node: Node):
        self.start_node = start_node
        self.open = []
        self.close = []

    def solve(self):
        if not self.start_node.is_solvable():
            raise ValueError('This puzzle is not solvable')
        self.open.append(self.start_node)
        while len(self.open) != 0:
            process = self._get_min_node()
            if process.get_h_score() == 0:
                self._print_path(self._get_path(process))
                return process
            self._remove_from_open(process)
            self.close.append(process)
            for state in process.find_other_coords():
                if self._find_node_in_close(state):
                    continue
                if not self._find_node_in_open(state):
                    state.set_predecessor(process)
                    self.open.append(state)
                else:
                    for i, opened in enumerate(self.open):
                        if opened.puzzle_data == state.puzzle_data and state.g_score < opened.g_score:
                            self.open[i].g_score = state.g_score
                            self.open[i].f_score = state.f_score
                            self.open[i].predecessor = state.predecessor

    def _get_min_node(self) -> Node:
        return sorted(self.open, key=lambda x: x.f_score, reverse=False)[0]

    def _remove_from_open(self, node):
        for i, state in enumerate(self.open):
            if state.puzzle_data == node.puzzle_data:
                del self.open[i]

    def _find_node_in_close(self, node):
        for state in self.close:
            if state.puzzle_data == node.puzzle_data:
                return True
        return False

    def _find_node_in_open(self, node):
        for state in self.open:
            if state.puzzle_data == node.puzzle_data:
                return True
        return False

    @staticmethod
    def _get_path(node: Node):
        result = [node]
        while node.predecessor:
            result.append(node.predecessor)
            node = node.predecessor
        return result[::-1]

    @staticmethod
    def _print_path(path):
        for i, node in enumerate(path):
            print(f'Step {i}')
            node.visualize_current_state()

# data = '''1 2 3\n0 4 6\n7 5 8'''.split('\n')
# data = [i.split(' ') for i in data]
#
# data1 = '''1 2 3 4
# 12 13 14 5
# 11 0 15 6
# 10 9 8 7'''.split('\n')
# data1 = [i.split(' ') for i in data1]
#
# data2 = '''1 2 3
# 8 0 4
# 7 6 5'''.split('\n')
# data2 = [i.split(' ') for i in data2]
#
# data3 = '''1 2 3 4 5
# 16 17 18 19 6
# 15 24 0 20 7
# 14 23 22 21 8
# 13 12 11 10 9'''.split('\n')
# data3 = [i.split(' ') for i in data3]
#
# # print(data in [data, data1])
# node = Node(puzzle_data=data3, g_score=0)
# game = Game(node)
# game.solve()