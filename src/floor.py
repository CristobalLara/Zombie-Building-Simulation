from .room import Room

class Floor:
    def __init__(self, floor_number: int, room_count: int, stairs_index: int = None):
        self.floor_number = floor_number
        self.rooms = [Room(i) for i in range(room_count)]

        # Asignar las escaleras solo si se proporciona un índice de escalera válido
        if stairs_index is not None and 0 <= stairs_index < room_count:
            self.rooms[stairs_index].stairs = True

    def get_room(self, room_number: int) -> Room:
        return self.rooms[room_number] if 0 <= room_number < len(self.rooms) else None

    def __str__(self):
        floor_status = f"Piso {self.floor_number}\n"
        for room in self.rooms:
            if room.stairs:
                stair_icon = "🔼"
            elif room.blocked:
                stair_icon = "🚫"
            else:
                stair_icon = "🚪" 
            floor_status += f" {stair_icon} {room}\n"
        return floor_status
    
    def to_dict(self):
        return {
            "rooms": [room.to_dict() for room in self.rooms]
        }

    def from_dict(self, data: dict):
        self.rooms = [
            Room(room_number=index).from_dict(room_data)
            for index, room_data in enumerate(data.get("rooms", []))
        ]
        return self