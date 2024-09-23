#!/bin/bash
set -o errexit  # Exit on error

apt-get update && apt-get install -y pkg-config libcairo2-dev

pip install --upgrade setuptools wheel

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
