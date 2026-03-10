from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

CLEAN_PATH = Path("data/processed/water_quality_cleaned.csv")
FIG_DIR = Path("outputs/figures")

def load_clean_data(path: Path) -> pd.DataFrame:
    """Load cleaned water quality data from a CSV file."""
    df = pd.read_csv(path)
    return df

def validate_expected_columns(df: pd.DataFrame) -> None:
    """Check that the cleaned dataset contains the required columns."""
    required = {"read_date", "water_temp_c", "dissolved_oxygen_mg_l", "ph", "air_temp_c"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {sorted(missing)}")
    
def print_summary_statistics(df: pd.DataFrame) -> None:
    """Print basic summary information about the cleaned dataset"""
    rows, cols = df.shape
    print("Dataset shape:")
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")

    dates = pd.to_datetime(df["read_date"], errors="coerce")
    date_min = dates.min()
    date_max = dates.max()
    print("\nDate range:")
    print(f"Start: {date_min}")
    print(f"End: {date_max}")

    summary_columns = ["salinity_ppt", "dissolved_oxygen_mg_l", "ph", "secchi_depth_m", "water_depth_m", "water_temp_c", "air_temp_c"]
    summary = df[summary_columns].describe()
    print("\nSummary statistics:")
    print(summary)

def plot_dissolved_oxygen_histogram(df: pd.DataFrame, out_path: Path) -> None:
    """Create and save a histogram of dissolved oxygen values"""
    plt.figure(figsize=(8,5))
    bins = range(0,18,1)
    df["dissolved_oxygen_mg_l"].dropna().plot(kind="hist",bins=bins, edgecolor="black")
    plt.title("Distribution of Dissolved Oxygen (mg/L)")
    plt.xlabel("Dissolved Oxygen (mg/L)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig(out_path, dpi=200)
    plt.close()

def plot_temp_vs_oxygen_scatter(df: pd.DataFrame, out_path: Path) -> None:
    """Create and save a scatter plot of water temperature vs dissolved oxygen"""
    plt.figure(figsize=(8,5))
    subset = df[["water_temp_c", "dissolved_oxygen_mg_l"]].dropna()
    plt.scatter(subset["water_temp_c"], subset["dissolved_oxygen_mg_l"], alpha=0.6)
    plt.title("Water Temperature vs Dissolved Oxygen")
    plt.xlabel("Water Temperature (°C)")
    plt.ylabel("Dissolved Oxygen (mg/L)")
    plt.tight_layout()

    plt.savefig(out_path, dpi=200)
    plt.close()

def plot_water_temperature_over_time(df: pd.DataFrame, out_path: Path) -> None:
    """Create and save a time-series plot of water temperature over time"""

    subset = df[["read_date", "water_temp_c"]].copy()
    subset["read_date"] = pd.to_datetime(subset["read_date"], errors="coerce")
    subset = subset.dropna(subset=["read_date", "water_temp_c"])
    subset = subset.sort_values("read_date")

    plt.figure(figsize=(10,5))
    plt.plot(subset["read_date"], subset["water_temp_c"])
    plt.title("Water Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Water Temperature (°C)")
    plt.tight_layout()
    
    plt.savefig(out_path, dpi=200)
    plt.close()

def plot_air_vs_water_temperature_scatter(df: pd.DataFrame, out_path: Path) -> None:
    """Produce a scatter plot of air temperature vs water temperature"""

    plt.figure(figsize=(8,5))
    subset = df[["air_temp_c", "water_temp_c"]].dropna()
    plt.scatter(subset["air_temp_c"], subset["water_temp_c"], alpha=0.6)
    plt.title("Air Temperature vs Water Temperature")
    plt.xlabel("Air Temperature (°C)")
    plt.ylabel("Water Temperature (°C)")
    plt.tight_layout()

    plt.savefig(out_path, dpi=200)
    plt.close()

def main():

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    df = load_clean_data(CLEAN_PATH)

    validate_expected_columns(df)

    print_summary_statistics(df)

    plot_dissolved_oxygen_histogram(df, FIG_DIR / "dissolved_oxygen_histogram.png")

    plot_temp_vs_oxygen_scatter(df, FIG_DIR/ "temp_vs_oxygen_scatter.png")

    plot_water_temperature_over_time(df, FIG_DIR / "water_temp_over_time.png")

    plot_air_vs_water_temperature_scatter(df, FIG_DIR / "air_vs_water_temp_scatter.png")

    print("Dataset loaded successfully")

if __name__ == "__main__":
    main()


