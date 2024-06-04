"""This module defines a maze with bombs"""

from maze_factory import MazeFactory
from maze_site import  Room, RoomWithABomb, Wall, BombedWall

class BombedMazeFactory(MazeFactory):
    """Defines a maze with bombs"""

    def make_wall(self) -> Wall:
        return BombedWall()

    def make_room(self, room_number: int) -> Room:
        return RoomWithABomb(room_number)
