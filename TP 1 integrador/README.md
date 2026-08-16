# TP 1 Integrador - Python

Este repositorio contiene el archivo `TP1_EsRepetitivas_LucianoVelasquez.py`, el cual corresponde al Trabajo Práctico Integrador de la materia Programación.

El programa incluye cinco ejercicios diferentes, cada uno desarrollado como una función independiente. En ellos se ponen en práctica estructuras de control iterativas (bucles `while` y `for`), condicionales y operaciones lógicas en Python.

Además, el repositorio incluye un archivo `.bat` que permite ejecutar el programa fácilmente desde una terminal de Windows o mediante doble clic.

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

Es un sistema simple de gestión de turnos para los días Lunes y Martes, implementado sin usar listas u otras colecciones avanzadas.

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
- En su turno, el jugador puede elegir entre:
  1. **Ataque Pesado:** Inflige 15 puntos de daño (o x1.5 si el enemigo tiene menos de 20 de vida).
  2. **Ráfaga Veloz:** Realiza 3 golpes de 5 puntos de daño cada uno.
  3. **Curar:** Usa una de las 3 pociones disponibles para recuperar 30 puntos de vida.
- Luego del turno del jugador, el enemigo ataca restando 12 puntos de vida.
- El bucle continúa hasta que la vida de alguno de los combatientes llegue a 0.

---

## Cómo ejecutar

### Opción 1: Ejecutar en Windows con el archivo `.bat`

El repositorio incluye un archivo `.bat` que permite ejecutar automáticamente el programa desde Windows.

Los archivos deben encontrarse en la misma carpeta:

```text
Repositorio/
│
├── TP1_EsRepetitivas_LucianoVelasquez.py
└── ejecutar_tp.bat
```

El archivo puede ejecutarse haciendo **doble clic sobre `ejecutar_tp.bat`**.

También puede ejecutarse desde CMD:

```cmd
ejecutar_tp.bat
```

O desde PowerShell:

```powershell
.\ejecutar_tp.bat
```

El archivo `.bat` verifica automáticamente que exista `TP1_EsRepetitivas_LucianoVelasquez.py` antes de intentar ejecutarlo.

### Opción 2: Ejecutar Python directamente

También es posible ejecutar el programa directamente desde una terminal de Windows:

```cmd
python TP1_EsRepetitivas_LucianoVelasquez.py
```

En instalaciones de Python que utilizan el launcher de Windows también se puede utilizar:

```cmd
py TP1_EsRepetitivas_LucianoVelasquez.py
```

> **Importante:** Python debe estar instalado y configurado correctamente en el sistema para poder ejecutar el programa.

Al ejecutarse, el script inicia un **menú interactivo por consola** que permite seleccionar y ejecutar cualquiera de los 5 ejercicios o salir del programa.