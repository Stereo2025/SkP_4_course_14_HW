from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR.joinpath('netflix_db', 'netflix.db')
