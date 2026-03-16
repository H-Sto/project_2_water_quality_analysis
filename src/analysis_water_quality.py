import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/processed/water_quality_cleaned.csv")
FIG_DIR = Path("outputs/figures")
TABLE_DIR = Path("outputs/tables")

def load_clean_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["read_date"] = pd.to_datetime(df["read_date"], errors="coerce")
    return df

def prepare_numeric_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select and return numeric columns for analysis."""
    numeric_df = df.select_dtypes(include="number").copy()
    return numeric_df


def main() -> None:
    df = load_clean_data(CLEAN_PATH)
    numeric_df = prepare_numeric_data(df)

if __name__ == "__main__":
    main()