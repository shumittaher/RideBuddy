#!/bin/bash
set -o errexit  # Exit on error

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input

# Apply database migrations
python3 manage.py migrate
