import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

APP_NAME = "Jarvis AI"

VERSION = "1.0"

WAKE_WORD = "jarvis"

DEBUG = True