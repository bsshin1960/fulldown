@echo off
echo =======================================
echo Building Global Dynamic PyQt6 App...
echo =======================================

:: Check PyInstaller
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller is not installed. Installing it now...
    pip install pyinstaller
)

:: Run PyInstaller with app icon
pyinstaller --noconfirm --onedir --windowed --icon="app_icon.ico" --name="Cursor메뉴_글로벌" menu_pyqt6_dynamic.py

echo =======================================
echo Build Completed!
echo Output executable resides in: dist\Cursor메뉴_글로벌\Cursor메뉴_글로벌.exe
echo =======================================
pause
