import random
import json

class Simulation:

    LEAVE_CHANCE = 0.5

    def __init__(self, building, save_file):
        self.building = building
        self.save_file = save_file

    def move_zombies(self):

        # Escanear y almacenar las habitaciones infestadas al inicio del turno
        infected_rooms = []
        for floor_index, floor in enumerate(self.building.floors):
            for room_index, room in enumerate(floor.rooms):
                if room.has_zombies:
                    infected_rooms.append((floor_index, room_index))  # Guardar índices para evitar el movimiento en cascada

        # Mover los zombis desde las habitaciones originalmente infestadas
        for floor_index, room_index in infected_rooms:
            room = self.building.floors[floor_index].rooms[room_index]

            # Almacenar habitaciones adyacentes
            adjacent_rooms = []
            
            # Habitación izquierda
            if room_index > 0:
                adjacent_rooms.append(self.building.floors[floor_index].rooms[room_index - 1])
            
            # Habitación derecha
            if room_index < len(self.building.floors[floor_index].rooms) - 1:
                adjacent_rooms.append(self.building.floors[floor_index].rooms[room_index + 1])
            
            # Habitación en el piso superior si hay escaleras
            if room.stairs and floor_index < len(self.building.floors) - 1:
                upstairs_room = self.building.floors[floor_index + 1].rooms[room_index]
                adjacent_rooms.append(upstairs_room)

            # Habitación en el piso inferior si hay escaleras
            if room.stairs and floor_index > 0:
                downstairs_room = self.building.floors[floor_index - 1].rooms[room_index]
                adjacent_rooms.append(downstairs_room)

            # Mover zombis a todas las habitaciones adyacentes no bloquedas
            for next_room in adjacent_rooms:
                if next_room.blocked:
                    continue
                next_room.add_zombies()
            
            # Probabilidad del 50% de vaciar la habitación original
            if random.random() < self.LEAVE_CHANCE:
                room.remove_zombies()

    def clean_room(self, floor_index: int, room_index: int):
        room = self.building.floors[floor_index].rooms[room_index]
        room.remove_zombies()

    def blocked_room(self, floor_index: int, room_index: int):
        room = self.building.floors[floor_index].rooms[room_index]
        room.blocked = True

    def reset_sensor(self, floor_index: int, room_index: int):
        room = self.building.floors[floor_index].rooms[room_index]
        room.reset_sensor()

    def save_state(self):
        with open(self.save_file, 'w') as f:
            json.dump(self.building.to_dict(), f, indent=4)
        print("Estado de la simulación guardado correctamente.")

    def display_status(self):
        print(self.building)

    def run(self):
        while True:
            self.display_status()
            print("\n1. Avanzar simulación (mover zombis)")
            print("2. Limpiar habitacion")
            print("3. Bloquear habitacion")
            print("4. Resetear sensor")
            print("5. Guardar sesion")
            print("6. Salir")
            choice = input("Elige una opción: ")

            if choice == "1":
                self.move_zombies()
                print("Zombis se han movido.")
            elif choice == "2":
                self.handle_room_action(self.clean_room, "limpiar")
            elif choice == "3":
                self.handle_room_action(self.blocked_room, "bloquear")
            elif choice == "4":
                self.handle_room_action(self.reset_sensor, "resetear el sensor")
            elif choice == "5":
                self.save_state()
            elif choice == "6":
                print("Saliendo de la simulación.")
                break
            else:
                print("Opción no válida.")

    def handle_room_action(self, action, action_name: str):
        try:
            floor_index = int(input("Elije el piso: "))
            room_index = int(input("Elije la habitación a {}: ".format(action_name)))
            action(floor_index, room_index)
            print(f"Habitación {room_index} en el piso {floor_index} ha sido {action_name}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        except IndexError:
            print("El piso o la habitación seleccionada no existen.")