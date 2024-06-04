"""This module hard codes how a maze is built"""

from maze import Maze
from maze_site import Room, Door, Wall, Direction
from maze_factory import MazeFactory

class MazeGame:
    """Hard codes the creation of a maze"""

    def create_maze(self) -> Maze:
        """Return a hard-coded maze"""
        _a_maze: Maze = Maze()
        r1: Room = Room(1)
        r2: Room = Room(2)
        the_door: Door = Door(r1, r2)

        _a_maze.add_room(r1)
        _a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, Wall())
        r1.set_side(Direction.EAST, the_door)
        r1.set_side(Direction.SOUTH, Wall())
        r1.set_side(Direction.WEST, Wall())

        r2.set_side(Direction.NORTH, Wall())
        r2.set_side(Direction.EAST, Wall())
        r2.set_side(Direction.SOUTH, Wall())
        r2.set_side(Direction.WEST, the_door)

        return _a_maze

    def create_maze_factory(self, factory: MazeFactory) -> Maze:
        """Uses the MazeFactory to create and return a Maze"""
        _a_maze:Maze = factory.make_maze()
        r1:Room = factory.make_room(1)
        r2:Room = factory.make_room(2)
        a_door: Door = factory.make_door(r1, r2)

        _a_maze.add_room(r1)
        _a_maze.add_room(r2)

        r1.set_side(Direction.NORTH, factory.make_wall())
        r1.set_side(Direction.EAST, a_door)
        r1.set_side(Direction.SOUTH, factory.make_wall())
        r1.set_side(Direction.WEST, factory.make_wall())

        r2.set_side(Direction.NORTH, factory.make_wall())
        r2.set_side(Direction.EAST, factory.make_wall())
        r2.set_side(Direction.SOUTH, factory.make_wall())
        r2.set_side(Direction.WEST, a_door)

        return _a_maze
