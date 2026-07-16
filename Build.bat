@echo off
title FenixPresence Builder

echo ================================
echo Building FenixPresence...
echo ================================

rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del /q *.spec 2>nul

py -m PyInstaller --onefile --noconsole --name FenixPresence --icon assets\fenix.ico main.py

echo.
echo ================================
echo Build finished!
echo Executable:
echo dist\FenixPresence.exe
echo ================================

pause