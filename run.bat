@echo off

echo Creating virtual environment...
python -m venv venv

echo Activating venv...
call venv\Scripts\activate

echo Installing requirements...
pip install -r requirements.txt

echo Running app...
python app.py

pause
