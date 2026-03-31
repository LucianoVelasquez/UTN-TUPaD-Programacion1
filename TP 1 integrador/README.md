# TP 1 Integrador - Python

Este repositorio contiene el archivo `TP1_EsRepetitivas_LucianoVelasquez.py`, el cual es un trabajo práctico integrador de la materia de Programación. El archivo incluye cinco ejercicios diferentes, cada uno desarrollado como una función independiente, que ponen en práctica el uso de estructuras de control iterativas (bucles `while` y `for`), condicionales y operaciones lógicas en Python.

## Descripción de los Ejercicios

### Ejercicio 1: “Caja del Kiosco” (`caja_kiosco()`)
Simula el funcionamiento de una caja registradora.
- Solicita y valida el nombre del cliente (solo letras).
- Pide la cantidad de productos a comprar.
- Por cada producto, solicita el precio y consulta si posee descuento (10%).
- Al final, muestra un ticket detallado con el cliente, cantidad de productos, total sin y con descuento, el ahorro logrado y el promedio gastado por producto.

### Ejercicio 2: “Acceso al Campus y Menú Seguro” (`acceso_seguro()`)
Implementa un sistema básico de autenticación de usuarios.
- Permite un máximo de 3 intentos para ingresar usuario (`alumno`) y contraseña (`python123`).
- Si el login es fallido 3 veces, la cuenta se bloquea.
- Si el acceso es exitoso, despliega un menú con la posibilidad de:
  1. Ver estado de inscripción.
  2. Cambiar clave (validando que tenga al menos 6 caracteres).
  3. Mostrar mensaje motivacional.
  4. Salir del sistema.

### Ejercicio 3: “Agenda de Turnos con Nombres” (`agenda_turnos()`)
Es un sistema simple de gestión de turnos para los días Lunes y Martes (implementado sin usar listas u otras colecciones avanzadas).
- **Reservar turno:** Asigna el nombre del paciente a un turno libre del día elegido.
- **Cancelar turno:** Libera el turno de un paciente indicando su nombre.
- **Ver agenda del día:** Imprime los turnos ocupados y libres de un día específico (Lunes o Martes).
- **Ver resumen general:** Muestra un panorama completo de los turnos de ambos días y determina qué día tuvo más pacientes asignados.

### Ejercicio 4: “Escape Room: La Bóveda” (`boveda()`)
Un minijuego de escape donde el objetivo es abrir 3 cerraduras antes de quedarse sin tiempo (12 turnos) o energía (100 puntos).
- **Forzar cerradura:** Gasta 20 de energía y 2 de tiempo. Si se fuerza 3 veces seguidas o con baja energía se elige la opción errónea, se activa una alarma.
- **Hackear panel:** Gasta 10 de energía y 3 de tiempo. Se pide ingresar una secuencia de letras para completar un código y abrir una cerradura de forma más segura.
- **Descansar:** Recupera energía y gasta tiempo. Si la alarma está activa la recuperación es menor.
- Si el jugador se queda sin energía o tiempo, o se bloquea la bóveda por alarma, pierde la partida.

### Ejercicio 5: “Escape Room: La Arena del Gladiador” (`arena()`)
Un juego de combate por turnos estilo RPG por consola.
- El jugador ("gladiador") se enfrenta a un enemigo, ambos con 100 puntos de vida.
- En tu turno, puedes elegir entre:
  1. **Ataque Pesado:** Inflige 15 puntos de daño (o x1.5 si el enemigo tiene menos de 20 de vida).
  2. **Ráfaga Veloz:** Realiza 3 golpes de 5 puntos de daño cada uno.
  3. **Curar:** Usa una de las 3 pociones disponibles para recuperar 30 puntos de vida.
- Luego del turno del jugador, el enemigo ataca restando 12 puntos de vida.
- El bucle continúa hasta que la vida de alguno de los combatientes llegue a 0.

---

## Cómo ejecutar

Para probar los ejercicios, simplemente puedes ejecutar el script de Python y llamar a la función correspondiente desde el propio código o interactuando en la terminal (actualmente, el script llama a `arena()` al final de su ejecución).

```bash
python TP1_EsRepetitivas_LucianoVelasquez.py
```
