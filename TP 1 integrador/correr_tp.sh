#!/bin/bash

# 1. Definir la ruta del archivo (ajustada para Ubuntu/WSL)
DIR_ACTUAL=$(dirname "$0")
ARCHIVO_PY="$DIR_ACTUAL/TP1_EsRepetitivas_LucianoVelasquez.py"

# Verificamos si el archivo existe antes de ejecutar
if [ -f "$ARCHIVO_PY" ]; then
    python3 "$ARCHIVO_PY"
else
    echo "Error: No se encontró el archivo de Python."
    echo "Asegúrate de estar dentro de la carpeta del repositorio."
fi

# 2. Imprimir un mensaje decorativo
echo "------------------------------------------"
echo "Lanzando TP de Luciano Velasquez..."
echo "------------------------------------------"

# 3. Ejecutar el programa con python3
# Usamos comillas dobles por si hay espacios en la ruta
python3 "$ARCHIVO_PY"

# 4. Mensaje final
echo "------------------------------------------"
echo "Ejecución finalizada."


