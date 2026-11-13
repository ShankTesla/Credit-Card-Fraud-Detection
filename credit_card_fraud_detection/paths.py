# credit_card_fraud_detection/paths.py

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SRC = ROOT / "credit_card_fraud_detection"
MODELING = SRC / "modeling"
DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA/ "interim"
PROCESSED = DATA / "processed"
EXTERNAL = DATA / "external"
LOGS = ROOT / "logs"
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"
MODELS = ROOT / "models"
TESTS = ROOT / "tests"

def dated(folder: Path, name: str, ext: str, day: date | None = None) -> Path:
    day = day or date.today()
    return folder / f"{name}_{day:%Y-%m-%d}.{ext.lstrip('.')}"