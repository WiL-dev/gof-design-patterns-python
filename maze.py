"""This module defines how a maze behaves"""

from maze_site import Room

class Maze:
    """Represents a collection of rooms"""
    def __init__(self) -> None:
        self._rooms: dict[int, Room] = {}

    def add_room(self, room: Room) -> None:
        """Add a room"""
        self._rooms[room.get_room_number()] = room

    def get_room(self, room_number: int) -> Room:
        """Returns a room given his number"""
        return self._rooms[room_number]

    def __str__(self) -> str:
        return "\n\n".join([str(room) for room_number, room in self._rooms.items()])
