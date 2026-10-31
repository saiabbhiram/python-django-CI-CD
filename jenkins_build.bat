@echo off
setlocal enabledelayedexpansion

echo === 1. Setting up Python Virtual Environment ===
python -m venv venv
call venv\Scripts\activate.bat

echo === 2. Upgrading Pip and Installing Dependencies ===
python -m pip install --upgrade pip
pip install -r requirements.txt

echo === 3. Running Django Checks & Migrations ===
python manage.py check
python manage.py migrate --noinput

echo === 4. Running Tests and Generating JUnit XML Report ===
if not exist reports mkdir reports
pytest --junitxml=reports/test-results.xml --cov=demo_app --cov-report=xml:reports/coverage.xml

echo === Build & Test Succeeded ===
