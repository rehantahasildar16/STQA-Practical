@echo off
cd /d "%~dp0"
title STQA Practical Automation Menu
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 RUN_STQA.py
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    python RUN_STQA.py
  ) else (
    echo Python is not installed or not added to PATH.
    echo Install Python first, then run this file again.
    pause
    exit /b 1
  )
)
pause
