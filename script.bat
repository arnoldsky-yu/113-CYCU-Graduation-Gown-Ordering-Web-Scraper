@echo off
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo "Python 未安裝，正在下載並安裝 Python..."
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe' -Verb RunAs"
    exit /b
)

pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo "安裝 pip..."
    python -m ensurepip --upgrade
)

pip install requests beautifulsoup4 pandas

python web_crawler.py

