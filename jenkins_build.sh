#!/usr/bin/env bash
set -e

echo "=== 1. Setting up Python Virtual Environment ==="
python3 -m venv venv
source venv/bin/activate

echo "=== 2. Upgrading Pip and Installing Dependencies ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== 3. Running Django Checks & Migrations ==="
python manage.py check
python manage.py migrate --noinput

echo "=== 4. Running Tests and Generating JUnit XML Report ==="
mkdir -p reports
pytest --junitxml=reports/test-results.xml --cov=demo_app --cov-report=xml:reports/coverage.xml

echo "=== Build & Test Succeeded ==="
