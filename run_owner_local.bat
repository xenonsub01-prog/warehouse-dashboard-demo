@echo off
cd /d %~dp0
if not exist venv\Scripts\activate.bat (
  echo Please run setup.bat first.
  pause
  exit /b 1
)
REM Load env vars
if exist .env (
  for /f "usebackq tokens=1,2 delims==" %%a in (".env") do set %%a=%%b
)
call venv\Scripts\activate
start "" http://localhost:8502/?admin=%OWNER_KEY%
streamlit run app.py --server.port=8502
