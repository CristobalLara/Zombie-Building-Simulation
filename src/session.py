from src.building import Building
from src.simulation import Simulation
import random
import json
import os

SAVE_FILE = 'simulation_state.json'

class Session:
    def __init__(self):
        self.start_session()

    def load_state(self) -> Building:
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, 'r') as f:
                    data = json.load(f)
                    
                    floors = len(data["floors"])
                    rooms_per_floor = len(data["floors"][0]["rooms"]) if floors > 0 else 0
                    
                    building = Building(floors, rooms_per_floor)
                    
                    for floor_index, floor_data in enumerate(data.get("floors", [])):
                        floor = building.get_floor(floor_index)
                        floor.from_dict(floor_data)
                    
                    print("Se encontró una sesión guardada.")
                    return building
            except (json.JSONDecodeError, AttributeError, KeyError) as e:
                print(f"Error al cargar el estado guardado: {e}")
        
        print("No se encontró un archivo de estado guardado o el archivo está corrupto. Iniciando nueva simulación.")
        return None

    def start_session(self):
        print("\nBienvenido a Zombie Survival Building!")

        building = self.load_state()
        load = "n"
        if building:
            load = input("\n¿Deseas cargar la sesión anterior? (Y/N)")

        if load.lower() != "y" or not building:
            floors = int(input("\nElige el número de pisos de tu edificio: "))
            rooms_per_floor = int(input("Elige el número de habitaciones por piso de tu edificio: "))
            
            building = Building(floors, rooms_per_floor)
            
            random_floor = random.randint(0, floors - 1)
            random_room = random.randint(0, rooms_per_floor - 1)
            
            building.get_floor(random_floor).get_room(random_room).add_zombies()

            print("\n¡Edificio creado con éxito!")

        simulation = Simulation(building, SAVE_FILE)
        simulation.run()