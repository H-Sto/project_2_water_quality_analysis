from clean_water_quality import main as clean_main
from eda_water_quality import main as eda_main
from pathlib import Path

def run_pipeline() -> None:

    print("Starting data cleaning...")
    clean_main()

    print("Data cleaning complete, starting exploratory data analysis...")
    eda_main()

    print("Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()