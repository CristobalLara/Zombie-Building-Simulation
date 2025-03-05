# Zombie Building Simulation

## Requisitos:
Python 3.11 o superior

## Instrucciones para Ejecutar:

Clona o descarga este repositorio.

Navega a la carpeta del proyecto en tu terminal.

El proyecto está configurado para ejecutarse como un paquete de Python. Para iniciar la simulación, utiliza el siguiente comando:

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
4. Desloquear habitación
5. Resetear sensor
6. Guardar sesión
7. Salir
Elige una opción:
A partir de aquí, puedes seleccionar lo que desees hacer.

## Comandos
La aplicación permite al usuario interactuar mediante un menú de opciones:

- Avanzar simulación (mover zombis): Los zombis se mueven a otras habitaciones adyacentes.
- Limpiar habitación: Se pueden limpiar habitaciones infestadas por zombis.
- Bloquear habitación: Las habitaciones pueden ser bloqueadas, evitando que los zombis se muevan a ellas.
- Desloquear habitación: Las habitaciones pueden ser desbloqueadas, permitiendo que los zombis se muevan a ellas.
- Resetear sensor: Resetea el sensor en una habitación.
- Guardar sesión: Guarda el estado actual del edificio en un archivo.
- Salir: Sale de la simulación.

## Leyenda
La aplicación utiliza simbolos para representar en consola los distintos elementos que la componen:
- Calavera ☠️: Representa una habitacion infestada de zombies.
- Alerta ❗: Representa un sensor en estado de alerta pero libre de zombies.
- Check Mark ✅: Representa un sensor en estado normal libre de zombies.
- Puerta 🚪: Representa una habitacion que puede ser infestada por zombies.
- Flecha 🔼: Representa una habitacion con escalera, es decir que permite infestar las habitaciones de arriba y abajo.
- Prohibido 🚫: Representa una habitacion bloqueda que no puede ser infestada por zombies.

## Funcionalidades

- Crear un edificio: Puedes crear un edificio con un número de pisos y habitaciones por piso.
- Simular el movimiento de los zombis: Los zombis se mueven entre habitaciones adyacentes.
- Interactuar con las habitaciones: El usuario puede limpiar, bloquear, desbloquear habitaciones o resetear los sensores.
- Guardar y cargar el estado de la simulación: El estado de la simulación puede guardarse en un archivo JSON para reanudarlo más tarde.
- Ver el estado del edificio: El estado de las habitaciones, zombis y sensores se muestra en la consola.

## Clases:
**Building**: Representa el edificio. Contiene múltiples pisos, cada uno con un número de habitaciones.

**Floor**: Representa un piso del edificio. Contiene varias habitaciones, cada una con características como el estado de los zombis, escaleras y bloqueos.

**Room**: Representa una habitación. Puede contener zombis y tiene un sensor para alertar de la presencia de zombis.

**Sensor**: Representa el sensor en cada habitación, que alerta cuando hay zombis presentes.

**Simulation**: Controla la lógica de la simulación, incluyendo el movimiento de los zombis, las acciones del usuario y la persistencia del estado del edificio.

**Session**: Inicia la simulacion desde las indicaciones del usuario o carga un archivo guardado.

**Main**: Punto de entrada del programa, donde se inicia la sesion del usuario.

## Arquitectura:
La arquitectura del sistema está basada en una estructura jerárquica en cadena de clases que representan el edificio, sus pisos, habitaciones y sensores:

- Cada Room tiene un Sensor que alerta si hay zombis en la habitación.
- Cada Floor tiene una lista de Room.
- Building tiene una lista de Floor.
- Simulation maneja el movimiento de los zombis entre las habitaciones y pisos, además de permitir que el usuario interactúe con las habitaciones (limpiar, bloquear, resetear sensores).
- Session carga un posible archivo guardado, o genera un edificio basado en las especificaciones del usuario.

## Consideraciones del Desarrollo:

Los Zombies tienen una probabilidad del 50% de abandonar por completo una habitaciones para invadir las habitaciones adyacentes o invadir las habitaciones y mantener la habitacion original infestada definida por la constante `LEAVE_CHANCE`.
Esto se establece en la linea 52 de simulation.py.

Se establecio el movimiento vertical de los zombies implementando la variable booleana `stairs` a los cuartos, si el valor de `stairs` es `True` la habitacion superior al cuarto se considera adyacente y los zombies pueden subir. Adicionalmente se decidio implementar una escalera principal por la cual se puede llegar desde el primer piso hasta el ultimo, igual que la estructura de un edificio normal. La ubicacion de la escalera se elije de manera aleatoria al generarse el edificio.

Los sensores se mantienen en `normal` siempre cuando no hayan detectado zombies, si detectan zombies se mantendran en `alert` hasta que sean reseteados por el usuario. El enunciado no especificaba si el sensor debia volver al estado normal si es que no detectaba zombies, solo que debia entrar en alerta al detectarlos.

Las acciones de los usuarios como limpiar, bloquear, desbloquear y resetear sensor, no avanzan los turnos de los zombies. El enunciado no especificaba si estas acciones causaban el movimiento de los zombies pero se hizo asi para poder ver con claridad el cambio realizado en el simulador.