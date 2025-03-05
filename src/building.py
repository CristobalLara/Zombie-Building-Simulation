from .floor import Floor
import random

class Building:
    def __init__(self, floor_count: int, rooms_per_floor: int):
        # Seleccionar un índice aleatorio para las escaleras en el primer piso
        self.stairs_index = random.randint(0, rooms_per_floor - 1)
        # Generar los pisos, pasando el mismo índice de escaleras a cada uno
        self.floors = [Floor(i, rooms_per_floor, self.stairs_index) for i in range(floor_count)]

    def get_floor(self, floor_number: int) -> Floor:
        return self.floors[floor_number] if 0 <= floor_number < len(self.floors) else None

    def __str__(self):
        return "\n".join([str(floor) for floor in reversed(self.floors)])
    
    def to_dict(self):
        return {
            "floors": [floor.to_dict() for floor in self.floors]
        }

    def from_dict(self, data: dict):
        self.floors = [Floor().from_dict(floor_data) for floor_data in data.get("floors", [])]
        return self