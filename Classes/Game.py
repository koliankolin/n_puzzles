from Node import Node

class Game:
    def __init__(self, start_node: Node):
        self.start_node = start_node
        self.open = []
        self.close = []

    def solve(self):
        self.open.append(self.start_node)
        while len(self.open) != 0:
            curr = self.open[0]
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

data = '''8 1 2
0 4 3
7 6 5'''.split('\n')
data = [i.split(' ') for i in data]

# data1 = '''1 2 3 4
# 12 13 14 5
# 11 0 15 6
# 10 9 8 7'''.split('\n')
# data1 = [i.split(' ') for i in data1]

# print(data in [data, data1])
node = Node(puzzle_data=data, g_score=0)
game = Game(node)
game.solve()