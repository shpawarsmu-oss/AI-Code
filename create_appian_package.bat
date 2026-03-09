@echo off
REM create_appian_package.bat
REM Double-click this file on Windows to create TestCodeSandbox_Appian.zip
REM Requires Python 3 to be installed and available on the system PATH.

echo ============================================================
echo  Appian Package Creator
echo ============================================================
echo.

REM Change to the directory where this batch file lives (repo root)
cd /d "%~dp0"

REM Check that Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python was not found. Please install Python 3 from:
    echo        https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Running create_appian_package.py ...
echo.
python create_appian_package.py

if errorlevel 1 (
    echo.
    echo ERROR: The script exited with an error. See output above.
    pause
    exit /b 1
)

echo.
echo Done! Import TestCodeSandbox_Appian.zip into Appian Designer.
echo.
pause
