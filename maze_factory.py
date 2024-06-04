"""
This module defines a factory
As is not an abstract class, it acts as both the AbstractFactory and the ConcreteFactory
"""
from maze import Maze
from maze_site import Wall, Room, Door

class MazeFactory:
    """Maze factory definition"""
    def make_maze(self) -> Maze:
        """Defines how to create a Maze"""
        return Maze()

    def make_wall(self) -> Wall:
        """Defines how to create a Wall"""
        return Wall()

    def make_room(self, room_number: int) -> Room:
        """Defines how to create a Room"""
        return Room(room_number)

    def make_door(self, room_1: Room, room_2: Room) -> Door:
        """Defines how to create a Door"""
        return Door(room_1, room_2)
