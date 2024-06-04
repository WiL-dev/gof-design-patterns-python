"""This module defines a Enchanted Maze Factory"""

from maze_factory import MazeFactory
from maze_site import Room, EnchantedRoom, Spell, DoorNeedingSpell

class EnchantedMazeFactory(MazeFactory):
    """Defines an Enchanted Maze"""

    def make_room(self, room_number: int) -> Room:
        """Defines how a Enchanted Room should be created"""
        return EnchantedRoom(room_number, self._cast_spell())

    def make_door(self, room_1, room_2):
        return DoorNeedingSpell(room_1, room_2)

    def _cast_spell(self) -> Spell:
        return Spell()
