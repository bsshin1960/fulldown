@echo off
echo ====================================================
echo Starting Local Web Server...
echo ====================================================
echo Click the link below or open in your browser:
echo http://localhost:8000/index_dynamic.html
echo ====================================================
echo Press Ctrl+C in this terminal window to stop the server.
echo ====================================================
python -m http.server 8000
pause
