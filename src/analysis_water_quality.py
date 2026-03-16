import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/processed/water_quality_cleaned.csv")
FIG_DIR = Path("outputs/figures")
TABLE_DIR = Path("outputs/tables")

def load_clean_data(path: Path) -> pd.DataFrame:

