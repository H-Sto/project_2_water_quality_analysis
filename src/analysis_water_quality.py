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

def main() -> None:
    df = load_clean_data(CLEAN_PATH)
    numeric_df = prepare_numeric_data(df)
    corr_matrix = calculate_correlation_matrix(numeric_df)
    plot_correlation_heatmap(corr_matrix, FIG_DIR / "correlation_heatmap.png")
    strong_corrs = find_strong_correlations(corr_matrix)

    print("\nStrongest correlations:")
    print(strong_corrs.head(10).round(2))
    strong_corrs.to_csv(TABLE_DIR / "strong_correlation.csv", index=False)


if __name__ == "__main__":
    main()