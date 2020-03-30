import sys
import getopt
from Classes.Parser import Parser
from Classes.Node import Node
from Classes.Game import Game

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f", ["file"])
    except getopt.error as msg:
        print(msg)
        print("It is necessary file :((")
        sys.exit(2)
    for arg in args:
        try:
            parser = Parser(file_name=arg)
            node = Node(puzzle_data=parser.get_data(), metric='manhattan')
            game = Game(start_node=node)
            game.solve()
            exit(0)
        except ValueError as error:
            print(error)
            exit(2)
    parser = Parser()
    node = Node(puzzle_data=parser.get_data(), metric='euclead')
    game = Game(start_node=node)
    game.solve()

if __name__ == "__main__":
    main()