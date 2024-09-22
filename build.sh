#!/bin/bash
set -o errexit  # Exit on error

# Upgrade pip
pip install --upgrade pip

# Install system dependencies
sudo apt-get update
sudo apt-get install -y pkg-config libcairo2-dev cmake

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
