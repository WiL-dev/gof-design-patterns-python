"""This module defines a maze with bombs"""

from maze import Maze
from maze_factory import MazeFactory
from maze_site import  Room, RoomWithABomb, Wall, BombedWall

class BombedMazeFactory(MazeFactory):
    """Defines a maze with bombs"""

    def make_wall(self) -> Wall:
        return BombedWall()

    def make_room(self, room_number: int) -> Room:
        return RoomWithABomb(room_number)

    #pylint: disable=useless-parent-delegation
    # Only 2 methods above are implemented for educational purposes
    def make_maze(self) -> Maze:
        return super().make_maze()

    def make_door(self, room_1: Room, room_2: Room):
        return super().make_door(room_1, room_2)
