#!/bin/bash

# Install dependencies and create virtual environment
uv sync --dev

# Add auto-activation to bashrc for new terminals
echo 'if [ -f .venv/bin/activate ]; then source .venv/bin/activate; fi' >> ~/.bashrc

# Activate for current session
source .venv/bin/activate