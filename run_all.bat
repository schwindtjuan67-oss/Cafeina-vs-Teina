@echo off
setlocal ENABLEDELAYEDEXPANSION

REM ==========================================================
REM  RUN_ALL.BAT - Todo en uno:
REM   - crea venv (.venv)
REM   - instala deps (requirements.txt o matplotlib)
REM   - corre mateina_vs_cafeina.py
REM   - muestra texto + abre imagen
REM ==========================================================

REM Ir a la carpeta del proyecto (donde está este .bat)
cd /d "%~dp0"

REM --- Config ---
set "VENV_DIR=.venv"
set "IMAGE_FILE=caffeine_structure.png"

REM --- Elegir python base (para crear venv) ---
REM Si "python" no está en PATH, poné ruta fija:
REM set "PYEXE=C:\Python314\python.exe"
set "PYEXE=python"

set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

echo ==========================================================
echo [0] Proyecto: %CD%
echo ==========================================================

REM --- Checks básicos de archivos ---
if not exist "mateina_vs_cafeina.py" (
  echo [ERROR] No existe mateina_vs_cafeina.py en esta carpeta.
  echo         Copialo aqui y volve a ejecutar.
  pause
  exit /b 1
)

if not exist "%IMAGE_FILE%" (
  echo [WARN] No existe %IMAGE_FILE% en esta carpeta.
  echo        El script correra igual pero no podra mostrar la imagen.
)

echo.
echo ==========================================================
echo [1/4] Verificando Python base...
echo ==========================================================
"%PYEXE%" --version
if errorlevel 1 (
  echo [ERROR] No se encontro Python. Ajusta PYEXE en este .bat o agrega Python al PATH.
  pause
  exit /b 1
)

echo.
echo ==========================================================
echo [2/4] Creando venv si no existe: %VENV_DIR%
echo ==========================================================
if not exist "%VENV_PY%" (
  "%PYEXE%" -m venv "%VENV_DIR%"
  if errorlevel 1 (
    echo [ERROR] Fallo al crear el venv.
    pause
    exit /b 1
  )
  echo [OK] venv creado.
) else (
  echo [OK] venv ya existe.
)

echo.
echo ==========================================================
echo [3/4] Instalando dependencias en el venv...
echo ==========================================================
"%VENV_PY%" -m pip install --upgrade pip
if errorlevel 1 (
  echo [ERROR] Fallo upgrade de pip.
  pause
  exit /b 1
)

REM Instala deps
if exist "requirements.txt" (
  echo [INFO] Instalando desde requirements.txt
  "%VENV_PY%" -m pip install -r "requirements.txt"
) else (
  echo [INFO] requirements.txt no encontrado. Instalando minimo: matplotlib
  "%VENV_PY%" -m pip install matplotlib
)

if errorlevel 1 (
  echo [ERROR] Fallo la instalacion de dependencias.
  pause
  exit /b 1
)

echo.
echo ==========================================================
echo [4/4] Corriendo demo (texto + imagen)...
echo ==========================================================
echo [INFO] Si hay matplotlib, la imagen se mostrara en una ventana.
echo [INFO] Si no, el script intentara abrirla con el visor de Windows.
echo.

"%VENV_PY%" "mateina_vs_cafeina.py" --image "%IMAGE_FILE%"
set "EXITCODE=%ERRORLEVEL%"

echo.
echo ==========================================================
echo Fin. ExitCode=%EXITCODE%
echo ==========================================================
echo.
pause
endlocal
exit /b %EXITCODE%
