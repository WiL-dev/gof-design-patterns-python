"""Hello world module"""

from enum import Enum
# from datetime import date

# import my_module as basic_module
# from my_connection import connect
# from my_bar import enter_club
from maze_game import MazeGame
# from bombed_maze_factory import BombedMazeFactory
from enchanted_maze_factory import EnchantedMazeFactory


class Weekdays(Enum):
    """Describes the weekdays"""
    MONDAY = 1

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])

if __name__ == "__main__":
    # basic_module.say_hi()
    # connect()
    # enter_club("Julio", 25, True)
    # enter_club("Bob", 25, True)
    # factory: BombedMazeFactory = BombedMazeFactory()
    factory: EnchantedMazeFactory = EnchantedMazeFactory()
    a_maze = MazeGame().create_maze_factory(factory)
    print(a_maze)
