@echo off

REM 1. Obtener la carpeta donde se encuentra este archivo .bat
set "DIR_ACTUAL=%~dp0"

REM 2. Definir la ruta del archivo Python
set "ARCHIVO_PY=%DIR_ACTUAL%TP1_EsRepetitivas_LucianoVelasquez.py"

REM 3. Mensaje inicial
echo ------------------------------------------
echo Lanzando TP de Luciano Velasquez...
echo ------------------------------------------

REM 4. Verificar si existe el archivo Python
if not exist "%ARCHIVO_PY%" (
    echo.
    echo ERROR: No se encontro el archivo de Python.
    echo Archivo esperado:
    echo "%ARCHIVO_PY%"
    echo.
    echo Asegurate de que el archivo .bat este dentro
    echo de la misma carpeta que el archivo Python.
    pause
    exit /b 1
)

REM 5. Ejecutar el programa
python "%ARCHIVO_PY%"

REM 6. Comprobar si hubo un error
if errorlevel 1 (
    echo.
    echo ------------------------------------------
    echo Ocurrio un error durante la ejecucion.
    echo ------------------------------------------
    pause
    exit /b 1
)

REM 7. Mensaje final
echo.
echo ------------------------------------------
echo Ejecucion finalizada.
echo ------------------------------------------

pause