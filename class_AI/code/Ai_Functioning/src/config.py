"""Configuration loader."""

import yaml
import os

# Determine project root (directory containing this file's parent config.yaml)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "config.yaml")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()