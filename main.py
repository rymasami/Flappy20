import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))

from Game import Game

if __name__ == "__main__":
    game = Game()
    game.run()