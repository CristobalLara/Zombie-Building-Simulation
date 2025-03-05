# Zombie Building Simulation

## Requisitos:
Python 3.11 o superior

## Instrucciones para Ejecutar:

Clona o descarga este repositorio.

Navega a la carpeta del proyecto en tu terminal y ejecuta el siguiente comando:

```
    python -m main
```

El programa te pedirá opciones para crear un nuevo edificio o cargar un edificio existente desde un archivo guardado.

Ejemplo de Uso
Cuando inicies la simulación, el programa te preguntará por el número de pisos y habitaciones por piso del edificio. Luego, podrás interactuar con el sistema usando las opciones del menú.

Ejemplo de Menú:

Bienvenido a Zombie Survival Building!

1. Avanzar simulación (mover zombis)
2. Limpiar habitación
3. Bloquear habitación
4. Resetear sensor
5. Guardar sesión
6. Salir
Elige una opción:
A partir de aquí, puedes seleccionar lo que desees hacer.

## Clases:
**Building**: Representa el edificio. Contiene múltiples pisos, cada uno con un número de habitaciones.

**Floor**: Representa un piso del edificio. Contiene varias habitaciones, cada una con características como el estado de los zombis, escaleras y bloqueos.

**Room**: Representa una habitación. Puede contener zombis y tiene un sensor para alertar de la presencia de zombis.

**Sensor**: Representa el sensor en cada habitación, que alerta cuando hay zombis presentes.

**Simulation**: Controla la lógica de la simulación, incluyendo el movimiento de los zombis, las acciones del usuario y la persistencia del estado del edificio.

**Main**: Punto de entrada del programa, donde el usuario puede iniciar una nueva simulación o cargar una sesión guardada.

## Arquitectura:
La arquitectura del sistema está basada en una estructura jerárquica de clases que representan el edificio, sus pisos, habitaciones y sensores:

- El Building tiene una lista de Floor.
- Cada Floor tiene una lista de Room.
- Cada Room tiene un Sensor que alerta si hay zombis en la habitación.
- La simulación maneja el movimiento de los zombis entre las habitaciones y pisos, además de permitir que el usuario interactúe con las habitaciones (limpiar, bloquear, resetear sensores).

## Funcionalidades

- Crear un edificio: Puedes crear un edificio con un número de pisos y habitaciones por piso.
- Simular el movimiento de los zombis: Los zombis se mueven entre habitaciones adyacentes.
- Interactuar con las habitaciones: El usuario puede limpiar, bloquear habitaciones o resetear los sensores.
- Guardar y cargar el estado de la simulación: El estado de la simulación puede guardarse en un archivo JSON para reanudarlo más tarde.
- Ver el estado del edificio: El estado de las habitaciones, zombis y sensores se muestra en la consola.

## Comandos
La aplicación permite al usuario interactuar mediante un menú de opciones:

- Avanzar simulación (mover zombis): Los zombis se mueven a otras habitaciones adyacentes.
- Limpiar habitación: Se pueden limpiar habitaciones infestadas por zombis.
- Bloquear habitación: Las habitaciones pueden ser bloqueadas, evitando que los zombis se muevan a ellas.
- Resetear sensor: Resetea el sensor en una habitación.
- Guardar sesión: Guarda el estado actual del edificio en un archivo.
- Salir: Sale de la simulación.

## Consideraciones del Desarrollo:

Los Zombies tienen una probabilidad del 50% de abandonar por completo una habitaciones para invadir las habitaciones adyacentes o invadir las habitaciones y mantener la habitacion original infestada definida por la constante `LEAVE_CHANCE`.
Esto se establece en la linea 52 de simulation.py.

