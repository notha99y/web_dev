import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(".") / "environment" / ".env")

DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or "sqlite:///" + str(
    Path(".") / "app.db"
)
