Warehouse Demo — Owner bypass + Short links (Port 8502)

Buttons
-------
- run_owner_local.bat   -> runs the app on http://localhost:8502 as OWNER (?admin=OWNER_KEY)
- run_owner_cloud.bat   -> opens your Streamlit Cloud URL as OWNER (reads CLOUD_URL or BASE_URL from .env)
- run_app.bat           -> normal run (local)

Env (.env)
----------
DEMO_SECRET=<auto/random>
OWNER_KEY=<auto/random or set your own>
BASE_URL=http://localhost:8502/
CLOUD_URL=https://your-app.streamlit.app/

Steps
-----
1) Double-click setup.bat
2) Double-click run_owner_local.bat  (Owner mode, local)
3) Or set CLOUD_URL then double-click run_owner_cloud.bat  (Owner mode, cloud)
4) Generate client Short URL from Admin Panel (visible only to Owner)
