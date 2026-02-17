@echo off
setlocal ENABLEDELAYEDEXPANSION
cd /d "%~dp0"

set "VENV_DIR=.venv"
set "PYEXE=python"
set "IMAGE_FILE=caffeine_structure.png"

echo ==========================================================
echo [0] Proyecto: %CD%
echo ==========================================================

echo.
echo ==========================================================
echo [1/4] Verificando Python base...
echo ==========================================================
%PYEXE% --version
if errorlevel 1 (
  echo [ERROR] No se encontro Python. Ajusta PYEXE o agrega Python al PATH.
  pause
  exit /b 1
)

echo.
echo ==========================================================
echo [2/4] Creando venv si no existe: %VENV_DIR%
echo ==========================================================
if not exist "%VENV_DIR%\Scripts\python.exe" (
  %PYEXE% -m venv "%VENV_DIR%"
  if errorlevel 1 (
    echo [ERROR] Fallo al crear el venv.
    pause
    exit /b 1
  )
  echo [OK] venv creado.
) else (
  echo [OK] venv ya existe.
)

set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

echo.
echo ==========================================================
echo [2.5/4] Verificando pip dentro del venv...
echo ==========================================================
"%VENV_PY%" -m pip --version >nul 2>&1
if errorlevel 1 (
  echo [WARN] pip NO esta disponible en el venv. Intentando reparar con ensurepip...
  "%VENV_PY%" -m ensurepip --upgrade >nul 2>&1
  "%VENV_PY%" -m pip --version >nul 2>&1
  if errorlevel 1 (
    echo [WARN] ensurepip no lo arreglo. Rehaciendo venv desde cero...
    rmdir /s /q "%VENV_DIR%" >nul 2>&1
    %PYEXE% -m venv "%VENV_DIR%"
    if errorlevel 1 (
      echo [ERROR] Fallo al recrear el venv.
      pause
      exit /b 1
    )
    set "VENV_PY=%VENV_DIR%\Scripts\python.exe"
    "%VENV_PY%" -m ensurepip --upgrade >nul 2>&1
    "%VENV_PY%" -m pip --version >nul 2>&1
    if errorlevel 1 (
      echo [ERROR] Sigue sin pip. Reinstala Python con pip+venv habilitados.
      pause
      exit /b 1
    )
  )
)
echo [OK] pip esta listo en el venv.

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

if exist "requirements.txt" (
  echo [INFO] Instalando desde requirements.txt
  "%VENV_PY%" -m pip install -r requirements.txt
) else (
  echo [INFO] requirements.txt no encontrado. (No hace falta matplotlib para localhost)
)

echo.
echo ==========================================================
echo [4/4] Levantando localhost...
echo ==========================================================
if not exist "app.py" (
  echo [ERROR] Falta app.py (crealo con el script que te pase).
  pause
  exit /b 1
)

echo [INFO] Abrira el navegador en http://127.0.0.1:8000/
echo [INFO] Para cerrar: CTRL+C en esta ventana.
echo.

"%VENV_PY%" app.py --image "%IMAGE_FILE%"
set "EXITCODE=%ERRORLEVEL%"

echo.
echo ==========================================================
echo Fin. ExitCode=%EXITCODE%
echo ==========================================================
pause
endlocal
exit /b %EXITCODE%
