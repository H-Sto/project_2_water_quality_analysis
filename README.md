# Water Quality Data Analysis

## Project Overview

This project analyses long-term water quality data from Back Bay National Wildlife Refuge (Virginia, USA) to identify environmental patterns and relationships between key variables.

The analysis progresses from data cleaning and exploratory data analysis (EDA) to more advanced analytical techniques, including correlation analysis and seasonal aggregation.

The project is designed as a **portfolio-quality data science workflow**, demonstrating:

- reproducible pipelines
- structured Python project design
- environmental data analysis
- clear communication of results

---

## Dataset

**Source:** Back Bay National Wildlife Refuge – Water Quality Monitoring Data  

The dataset contains measurements recorded between **1989 and 2019**, including:

- Salinity (ppt)
- Dissolved Oxygen (mg/L)
- pH
- Secchi Depth (water clarity)
- Water Depth (m)
- Water Temperature (°C)
- Air Temperature (°C)
- Date of observation

Raw data location:
# Water Quality Data Analysis

## Project Overview

This project analyses long-term water quality data from Back Bay National Wildlife Refuge (Virginia, USA) to identify environmental patterns and relationships between key variables.

The analysis progresses from data cleaning and exploratory data analysis (EDA) to more advanced analytical techniques, including correlation analysis and seasonal aggregation.

The project is designed as a **portfolio-quality data science workflow**, demonstrating:

- reproducible pipelines
- structured Python project design
- environmental data analysis
- clear communication of results

---

## Dataset

**Source:** Back Bay National Wildlife Refuge – Water Quality Monitoring Data  

The dataset contains measurements recorded between **1989 and 2019**, including:

- Salinity (ppt)
- Dissolved Oxygen (mg/L)
- pH
- Secchi Depth (water clarity)
- Water Depth (m)
- Water Temperature (°C)
- Air Temperature (°C)
- Date of observation

Raw data location:
data/raw/BKB_WaterQualityData_2020084.csv


---

## Project Structure
project-2-water-quality-analysis/

├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned dataset
│
├── outputs/
│ ├── figures/ # Generated plots
│ └── tables/ # Analysis outputs
│
├── src/
│ ├── clean_water_quality.py # Data cleaning
│ ├── eda_water_quality.py # Exploratory analysis
│ ├── analysis_water_quality.py # Advanced analysis
│ └── run_pipeline.py # Full pipeline controller
│
├── notebooks/ # Optional exploration
├── requirements.txt
└── README.md


---

## Analysis Goals

This project investigates:

- How water quality variables vary over time
- Whether clear **seasonal patterns** exist
- Relationships between key variables:
  - water temperature vs dissolved oxygen
  - air temperature vs water temperature
- Which variables are most strongly correlated
- How aggregation (monthly averages) improves interpretability

---

## Methods

The project follows a **three-stage reproducible pipeline**.

### 1. Data Cleaning

- Standardise column names
- Convert variables to correct data types
- Handle missing and invalid values
- Extract time-based features (year, month)
- Save cleaned dataset

---

### 2. Exploratory Data Analysis (EDA)

- Summary statistics
- Distribution plots
- Scatter plots of key relationships
- Time-series visualisation

---

### 3. Advanced Analysis

- Correlation matrix of numeric variables
- Heatmap visualisation of correlations
- Extraction of strongest variable relationships
- Filtering correlations by threshold
- Monthly aggregation of key variables
- Seasonal visualisations:
  - monthly water temperature
  - monthly dissolved oxygen
  - combined temperature vs oxygen plot

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt

Run the full pipeline:

python src/run_pipeline.py

python src/run_pipeline.py

outputs/figures/
outputs/tables/