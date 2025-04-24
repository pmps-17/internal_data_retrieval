# tests/conftest.py
import os
import sys

# Prepend the project root (one level up from tests/) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
