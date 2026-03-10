# Water Quality Data Analysis

## Project Overview

This project performs an exploratory data analysis (EDA) of long-term water quality measurements collected from monitoring sites at Back Bay National Wildlife Refuge (Virginia, USA).

The dataset contains observations of multiple environmental variables including salinity, dissolved oxygen, pH, water temperature, air temperature, water depth, and water clarity.

The goal of this project is to explore patterns in water quality measurements over time and investigate relationships between key environmental variables.

This project was developed as part of a structured portfolio-building workflow to demonstrate reproducible data analysis using Python.

---

## Dataset

Source: Back Bay National Wildlife Refuge – Water Quality Monitoring Data

The dataset contains measurements recorded between **1989 and 2019** across monitoring sites and includes variables such as:

- Salinity (ppt)
- Dissolved Oxygen (mg/L)
- pH
- Secchi Depth (water clarity)
- Water Depth
- Water Temperature
- Air Temperature
- Date of observation

The raw dataset is stored in:

data/raw/BKB_WaterQualityData_2020084.csv

---

## Project Structure

project-2-water-quality-analysis

data  
raw – original dataset  
processed – cleaned dataset  

outputs  
figures – generated visualisations  

src  
clean_water_quality.py – data cleaning pipeline  
eda_water_quality.py – exploratory data analysis  
run_pipeline.py – executes the full workflow  

notebooks – optional exploratory notebooks  

requirements.txt – Python dependencies  
README.md – project documentation  

---

## Analysis Goals

This project explores several questions:

- How do key water quality indicators vary over time?
- Are there seasonal patterns in water temperature?
- What relationships exist between environmental variables such as:
  - water temperature and dissolved oxygen
  - air temperature and water temperature
- What are the distributions of major water quality parameters?

---

## Methods

The analysis follows a reproducible pipeline consisting of two main stages.

### Data Cleaning

- Load the raw dataset
- Standardise column names
- Convert variables to appropriate data types
- Handle missing or invalid values
- Save a cleaned dataset for analysis

### Exploratory Data Analysis

- Summary statistics for water quality variables
- Distribution visualisations
- Time-series analysis
- Scatter plots exploring relationships between environmental variables

All analysis scripts are located in the `src` directory.

---

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run the analysis pipeline:

python src/run_pipeline.py

Generated visualisations will be saved to:

outputs/figures/

---

## Key Outputs

The analysis generates several visualisations including:

- Distribution of dissolved oxygen levels
- Distribution of pH values
- Water temperature trends over time
- Relationship between air temperature and water temperature
- Relationship between water temperature and dissolved oxygen

---

## Future Improvements

Possible extensions of this project include:

- Seasonal decomposition of time series
- Site-level comparison of water quality
- Correlation analysis between variables
- Predictive modelling of water temperature or dissolved oxygen

---

## Author

Portfolio data analysis project developed to demonstrate reproducible environmental data analysis using Python.