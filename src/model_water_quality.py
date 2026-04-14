"""Basic modelling for water quality prediction."""

# First modelling task:
# Predict dissolved oxygen from water temperature
# using a simple linear regression model.

# Target variable (y):
# dissolved_oxygen_mg_l

# Predictor variable (X):
# water_temp_c

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "water_quality_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

def load_data(path:Path) -> pd.DataFrame:
    """Load the cleaned water quality dataset"""
    df = pd.read_csv(path)
    return(df)

def prepare_modelling_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select and clean the variables needed for regression modelling"""
    model_df = df[["water_temp_c", "dissolved_oxygen_mg_l"]].copy()
    model_df = model_df.dropna()
    return model_df


def main() -> None:
    df = load_data(DATA_PATH)
    model_df = prepare_modelling_data(df)
    print("Modelling dataset shape:")
    print(model_df.shape)
    print(model_df.head())

if __name__ == "__main__":
    main()