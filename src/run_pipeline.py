from clean_water_quality import main as clean_main
from eda_water_quality import main as eda_main
from analysis_water_quality import main as analysis_main
from model_water_quality import main as model_main

def run_pipeline() -> None:

    print("Starting data cleaning...")
    clean_main()

    print("Data cleaning complete, starting exploratory data analysis...")
    eda_main()

    print("Exploratory data analysis complete, starting further analysis...")
    analysis_main()

    print("Further analysis complete, starting modelling...")
    model_main()

    print("Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()