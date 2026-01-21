@echo off
chcp 65001 >nul
cls
echo ========================================
echo   GitHub Repos Collector
echo   Instalando dependências...
echo ========================================
echo.
pip install -r requirements.txt
echo.
echo ========================================
echo   Instalação concluída!
echo   Execute "iniciar.bat" para começar
echo ========================================
pause
