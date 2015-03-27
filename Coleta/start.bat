echo off
set PYTHON_HOME=C:/Python27
set SCRIPT_HOME=C:/Users/xb146806/workspace_new/Coleta
set WEBSPHERE_HOME=C:/IBM/WebSphere/AppServer

set PATH=%WEBSPHERE_HOME%/bin;%PATH%

cd %SCRIPT_HOME%
cls
echo.
echo ===================================
echo == Geracao de Status do Ambiente ==
echo ===================================
echo.
pause
%PYTHON_HOME%/python.exe Executa_status.py
pause