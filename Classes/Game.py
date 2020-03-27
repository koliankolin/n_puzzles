from Classes.Node import Node

class Game:
    def __init__(self, start_node: Node):
        self.start_node = start_node
        self.open = []
        self.close = []

    def solve(self):
        if not self.start_node.is_solvable():
            raise ValueError('This puzzle is not sovable')
        self.open.append(self.start_node)
        idx = 1
        print('\nBegin solving')
        while len(self.open) != 0:
            curr = self.open[0]
            print(f'Step {idx}')
            curr.visualize_current_state()
            print()
            if curr.get_h_score() == 0:
                return curr
            else:
                del self.open[0]
                for i in curr.find_other_coords():
                    if i.puzzle_data not in self.close and i not in [i.puzzle_data for i in self.open]:
                        self.open.append(i)
                self.open.sort(key=lambda x: x.f_score, reverse=False)
                self.close.append(curr.puzzle_data)
                idx += 1

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