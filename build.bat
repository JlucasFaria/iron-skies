@echo off
echo === IronSkies - Compilacao para .exe ===

echo Instalando PyInstaller...
py -m pip install pyinstaller

echo Compilando...
py -m PyInstaller --onefile --windowed --add-data "assets;assets" --name "IronSkies" main.py

echo.
echo Pronto! O executavel esta em: dist\IronSkies.exe
echo Copie a pasta assets\ para junto do .exe antes de entregar.
pause
