"""This module defines all possible maze sites"""

from abc import ABC, abstractmethod
from enum import Enum
from random import randint

Direction = Enum("Direction", ["NORTH", "EAST", "SOUTH", "WEST"], start=0)

class MazeSite(ABC):
    """Base class for all possible maze sites"""

    @abstractmethod
    def enter(self):
        """Override to define the action to perform for an specific site"""

class Room(MazeSite):
    """A room changes your position when you enter on it"""
    def __init__(self, room_number: int) -> None:
        """room_number is used to locate a room"""
        self._room_number: int = room_number
        self._sides: list[MazeSite] = [None] * len(Direction)

    def enter(self) -> None:
        """Action performed when you enter the room"""
        print(f"You have entered room {self._room_number}")

    def get_side(self, direction: Direction) -> MazeSite:
        """Returns the a side given a direction"""
        return self._sides[direction.value]

    def set_side(self, direction: Direction, maze_site: MazeSite) -> None:
        """Set the side of the room using the site"""
        self._sides[direction.value] = maze_site

    def get_room_number(self) -> int:
        """Returns the room numbers"""
        return self._room_number

    def __str__(self) -> str:
        return  (
            f"Room {self.get_room_number()}\n"
            f"To the north there is a {self.get_side(Direction.NORTH)}\n"
            f"To the east there is a {self.get_side(Direction.EAST)}\n"
            f"To the south there is a {self.get_side(Direction.SOUTH)}\n"
            f"To the west there is a {self.get_side(Direction.WEST)}"
        )

class Spell:
    """Creates a random spell"""
    def __init__(self) -> None:
        self._spell_number = randint(1,500)

    def __str__(self) -> str:
        return f"Spell n. {self._spell_number}"

class EnchantedRoom(Room):
    """Extends a Room adding the faculty of having enchanted items"""
    def __init__(self, room_number: int, spell: Spell) -> None:
        super().__init__(room_number)
        self._spell: Spell = spell

    def __str__(self) -> str:
        return super().__str__() + f"\nContains {str(self._spell)}"

class RoomWithABomb(Room):
    """Extends a Room adding a bomb inside"""

    def __str__(self) -> str:
        return super().__str__() + "\nA bomb inside can explode in any moment..."

class Wall(MazeSite):
    """Defines a wall"""
    def enter(self) -> None:
        """Action performed when you try to enter in a wall"""
        print("You cannot go through a wall")

    def __str__(self) -> str:
        return "wall"

class BombedWall(Wall):
    """Extends a wall to create a wall that can be bombed"""
    def __str__(self) -> str:
        return super().__str__() + " - can be bombed"

class Door(MazeSite):
    """Defines how to go through a door"""
    def __init__(self, room_1: Room, room_2: Room) -> None:
        self._room_1 = room_1
        self._room_2 = room_2

    def other_side_from(self, reference_room: Room) -> Room:
        """Returns the other side of the door from the reference_room"""
        return self._room_1 if self._room_1 == reference_room else self._room_2

    def enter(self) -> None:
        """Action performed when pass through a door"""
        print("You have crossed a door")

    def __str__(self) -> str:
        return (
            "door"
            f"\n ∟ one side is room {self._room_1.get_room_number()} "
            f"on the other room {self._room_2.get_room_number()}"
        )

class DoorNeedingSpell(Door):
    """Extends a door to asks for a spell to be opened"""
    def __str__(self) -> str:
        return super().__str__() + " - needs a spell to be opened"

if __name__ == "__main__":
    test_room = Room(1)
    next_room = Room(2)
    test_direction = Direction.NORTH


    test_room.set_side(test_direction, next_room)
    assert test_room.get_side(test_direction) == next_room, \
        f"Room to the {test_direction.name} should be eq to next_room"
    test_room.enter()
