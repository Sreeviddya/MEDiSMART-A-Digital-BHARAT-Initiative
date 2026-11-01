from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent

# Subdirectories
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
MODULES_DIR = BASE_DIR / "modules"
ARCHIVE_DIR = BASE_DIR / "archive"

# Key File Paths
LOGO_PATH = ASSETS_DIR / "logo.jpg"
DB_PATH = BASE_DIR / "health_records.db"