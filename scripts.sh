#!/bin/bash

# Pytest c/ Cobertura
python -m pytest --cov=src -v

python -m pytest --cov=src --cov-report=html

python -m pytest --cov=src --cov-report=xml:coverage.xml --junitxml=test-results.xml

