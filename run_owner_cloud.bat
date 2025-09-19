@echo off
cd /d %~dp0
REM Opens your deployed Streamlit Cloud app as OWNER
REM Set CLOUD_URL in .env (e.g., https://your-app.streamlit.app/)
set TARGET=%CLOUD_URL%
if "%TARGET%"=="" set TARGET=%BASE_URL%
if "%TARGET%"=="" set TARGET=https://your-app.streamlit.app/
REM Load env vars
if exist .env (
  for /f "usebackq tokens=1,2 delims==" %%a in (".env") do set %%a=%%b
)
start "" %TARGET%?admin=%OWNER_KEY%
