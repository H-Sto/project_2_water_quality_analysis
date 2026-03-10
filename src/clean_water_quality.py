from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/BKB_WaterQualityData_2020084.csv")
PROCESSED_PATH = Path("data/processed/water_quality_cleaned.csv")


def load_raw_data(path: Path) -> pd.DataFrame:
    """Load raw water quality data from a CSV file."""
    return pd.read_csv(path)


def standardise_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise column names for easier analysis."""
    df = df.copy()

    df = df.rename(
        columns={
            "Site_Id": "site_id",
            "Unit_Id": "unit_id",
            "Read_Date": "read_date",
            "Salinity (ppt)": "salinity_ppt",
            "Dissolved Oxygen (mg/L)": "dissolved_oxygen_mg_l",
            "pH (standard units)": "ph",
            "Secchi Depth (m)": "secchi_depth_m",
            "Water Depth (m)": "water_depth_m",
            "Water Temp (?C)": "water_temp_c",
            "Air Temp-Celsius": "air_temp_c",
            "Air Temp (?F)": "air_temp_f",
            "Time (24:00)": "time_2400",
            "Field_Tech": "field_tech",
            "DateVerified": "date_verified",
            "WhoVerified": "who_verified",
            "AirTemp (C)": "air_temp_c_alt",
            "Year": "year_raw",
        }
    )
    return df


def clean_water_quality_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean water quality data for analysis."""
    df = df.copy()

    df["site_id"] = df["site_id"].str.strip().str.upper()
    df["unit_id"] = df["unit_id"].astype(str).str.strip().str.upper()

    df["read_date"] = pd.to_datetime(df["read_date"], errors="coerce")

    numeric_columns = [
        "salinity_ppt",
        "dissolved_oxygen_mg_l",
        "ph",
        "secchi_depth_m",
        "water_depth_m",
        "water_temp_c",
        "air_temp_c",
        "air_temp_f",
        "air_temp_c_alt",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["year"] = df["read_date"].dt.year.astype("Int64")
    df["month"] = df["read_date"].dt.month.astype("Int64")

    columns_to_drop = [
        "field_tech",
        "date_verified",
        "who_verified",
        "time_2400",
        "air_temp_f",
        "air_temp_c_alt",
        "year_raw",
    ]

    df = df.drop(columns=columns_to_drop, errors="ignore")
    df = df.dropna(subset=["read_date"])

    return df


def save_cleaned_data(df: pd.DataFrame, path: Path) -> None:
    """Save the cleaned water quality data to a CSV file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def main() -> None:
    df_raw = load_raw_data(RAW_PATH)
    df_renamed = standardise_column_names(df_raw)
    df_cleaned = clean_water_quality_data(df_renamed)
    save_cleaned_data(df_cleaned, PROCESSED_PATH)

    print("Raw dataset loaded successfully.")
    print(f"Rows in raw dataset: {len(df_raw)}")
    print(f"Rows in cleaned dataset: {len(df_cleaned)}")
    print("\nCleaned columns:")
    print(df_cleaned.columns.tolist())
    print(f"\nSaved cleaned dataset to: {PROCESSED_PATH}")


if __name__ == "__main__":
    main()