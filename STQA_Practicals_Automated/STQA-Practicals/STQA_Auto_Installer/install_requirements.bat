@echo off
title STQA Practicals - Automatic Requirements Installer
cd /d "%~dp0"

echo ==========================================
echo   STQA PRACTICALS - AUTOMATIC INSTALLER
echo ==========================================
echo.

where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=py"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set "PYTHON_CMD=python"
    ) else (
        echo ERROR: Python is not installed or not added to PATH.
        echo Please install Python first, then run this file again.
        echo Download: https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

echo Checking Python...
%PYTHON_CMD% --version
if errorlevel 1 (
    echo ERROR: Python could not be started.
    pause
    exit /b 1
)

echo.
echo Checking pip...
%PYTHON_CMD% -m pip --version
if errorlevel 1 (
    echo pip is missing. Trying to enable pip...
    %PYTHON_CMD% -m ensurepip --upgrade
    if errorlevel 1 (
        echo ERROR: Could not enable pip.
        pause
        exit /b 1
    )
)

echo.
echo Installing required Python libraries...
%PYTHON_CMD% -m pip install -r "%~dp0requirements.txt"
if errorlevel 1 (
    echo.
    echo INSTALLATION FAILED.
    echo Check your internet connection and Python version.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo   ALL PYTHON LIBRARIES INSTALLED
echo ==========================================
echo.
echo Installed packages:
%PYTHON_CMD% -m pip show selenium openpyxl pytest pytest-html locust
echo.
echo NOTE: Chrome, Java JDK, Selenium Server and Jenkins
echo are separate software and are not installed by pip.
echo.
pause
