@echo off
chcp 65001 >nul
title Catalog of Books - Flask Server
color 0B

echo ========================================
echo     BOOK CATALOG LAUNCH
echo ========================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not installed!
    echo Download Python from https://python.org
    pause
    exit
)

:: Create virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
)

:: Activate environment
echo Activating environment...
call venv\Scripts\activate

:: Install dependencies
echo Installing Flask...
pip install -r requirements.txt

:: Initialize database
echo Initializing database...
python database.py

:: Run server
echo.
echo ========================================
echo SERVER RUNNING!
echo Open in browser:
echo http://127.0.0.1:5000
echo Admin panel: http://127.0.0.1:5000/admin
echo ========================================
echo.
echo Press Ctrl+C to stop server
echo.

python app.py

pause