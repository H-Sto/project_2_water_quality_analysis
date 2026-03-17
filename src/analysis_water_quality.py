import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
plt.style.use("ggplot")

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
    numeric_df = numeric_df.drop(columns=["year", "month"], errors = "ignore")
    return numeric_df

def calculate_correlation_matrix(df:pd.DataFrame) -> pd.DataFrame:
    """Calculate and return the correlation matrix for numeric variables."""
    corr_matrix = df.corr()
    return corr_matrix

def plot_correlation_heatmap(corr_matrix: pd.DataFrame, out_path: Path) -> None:
    """Create and save a heatmap visualising correlations between variables"""
    plt.figure(figsize=(10,8))
    plt.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(label="Correlation Coefficient")
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    plt.title("Correlation Heatmap of Water Quality Variables")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

def find_strong_correlations(corr_matrix: pd.DataFrame) -> pd.DataFrame:
    """Return a table of the strongest variable correlations."""
    corr_long = corr_matrix.unstack().reset_index()
    corr_long.columns = ["variable_1", "variable_2", "correlation"]
    corr_long = corr_long[corr_long["variable_1"] != corr_long["variable_2"]]
    
    corr_long["pair_key"] = corr_long.apply(lambda row: tuple(sorted([row["variable_1"], row["variable_2"]])),axis=1)

    corr_long = corr_long.drop_duplicates(subset="pair_key")

    corr_long["abs_correlation"] = corr_long["correlation"].abs()
    corr_long = corr_long.sort_values("abs_correlation", ascending=False)

    corr_long = corr_long.drop(columns=["pair_key", "abs_correlation"])

    return corr_long

def filter_correlations(strong_corrs: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """Filter correlations by absolute value threshold."""
    filtered = strong_corrs[strong_corrs["correlation"].abs() >= threshold]
    return filtered

def calculate_monthly_averages(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate monthly mean values for selected water quality variables."""
    subset = df[["month", "water_temp_c", "dissolved_oxygen_mg_l"]].copy()
    subset = subset.dropna(subset=["month"])
    monthly_summary = subset.groupby("month")[["water_temp_c", "dissolved_oxygen_mg_l"]].mean()
    monthly_summary = monthly_summary.reset_index()
    return monthly_summary

def plot_monthly_water_temperature(monthly_df: pd.DataFrame, out_path:Path) -> None:
    """Plot monthly average water temperature."""
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    plt.figure(figsize=(8,5))
    plt.plot(monthly_df["month"], monthly_df["water_temp_c"], marker="o")
    plt.xticks(ticks=monthly_df["month"], labels=month_labels)
    plt.title("Average Water Temperature by Month")
    plt.xlabel("Month")
    plt.ylabel("Water Temperature (°C)")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

def plot_monthly_dissolved_oxygen(monthly_df: pd.DataFrame, out_path: Path) -> None:
    """Plot monthly dissolved oxygen"""
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    plt.figure(figsize=(8,5))
    plt.plot(monthly_df["month"], monthly_df["dissolved_oxygen_mg_l"], marker="o")
    plt.xticks(ticks=monthly_df["month"], labels=month_labels)
    plt.title("Average Dissolved Oxygen by Month")
    plt.xlabel("Month")
    plt.ylabel("Dissolved Oxygen (mg/L)")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()

def main() -> None:

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)

    df = load_clean_data(CLEAN_PATH)
    numeric_df = prepare_numeric_data(df)
    corr_matrix = calculate_correlation_matrix(numeric_df)
    plot_correlation_heatmap(corr_matrix, FIG_DIR / "correlation_heatmap.png")
    strong_corrs = find_strong_correlations(corr_matrix)

    strong_corrs.to_csv(TABLE_DIR / "strong_correlation.csv", index=False)
    filtered_corrs = filter_correlations(strong_corrs, threshold=0.3)

    filtered_corrs.to_csv(TABLE_DIR / "filtered_correlations.csv", index=False)
    monthly_summary = calculate_monthly_averages(df)

    monthly_summary.to_csv(TABLE_DIR / "monthly_average.csv", index=False)

    plot_monthly_water_temperature(monthly_summary, FIG_DIR / "monthly_water_temperature.png")

    plot_monthly_dissolved_oxygen(monthly_summary, FIG_DIR / "monthly_dissolved_oxygen.png")

if __name__ == "__main__":
    main()