#!/bin/bash
set -o errexit  # Exit on error

apt-get update && apt-get install -y pkg-config libcairo2-dev

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input

# Apply database migrations
python3 manage.py migrate
