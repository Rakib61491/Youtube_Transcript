#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating venv..."
source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Running app..."
python app.py
