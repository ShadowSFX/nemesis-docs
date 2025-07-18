@echo off
echo ========================================
echo   Sistema Nemesis Documentation
echo   Live Preview Server
echo ========================================
echo.
echo Starting live preview server...
echo Open your browser to: http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
sphinx-autobuild source build/html --open-browser 