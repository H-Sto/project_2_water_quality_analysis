# Water Quality Exploratory Data Analysis

## Project Overview

This project performs exploratory data analysis (EDA) on long-term water quality monitoring data.
The dataset contains measurements of physical and chemical water properties collected at monitoring sites over time.

The goal of the project is to explore patterns in water quality measurements, investigate relationships between environmental variables, and demonstrate a reproducible data analysis workflow using Python.

---

## Dataset

Source: Kaggle – Water Quality Data
The dataset includes environmental monitoring measurements such as:

* Salinity (ppt)
* Dissolved Oxygen (mg/L)
* pH
* Secchi Depth (water transparency)
* Water Temperature
* Air Temperature
* Water Depth
* Measurement date and site identifiers

Observations span multiple years of monitoring data.

---

## Project Goals

The analysis explores several key questions:

* How do water quality measurements vary over time?
* Are there seasonal patterns in water temperature?
* What relationships exist between environmental variables?
* How do dissolved oxygen levels relate to water temperature?
* How closely do air temperature and water temperature track one another?

---

## Methods

The project follows a reproducible data analysis pipeline:

1. **Data Cleaning**

   * Standardize column names
   * Convert data types
   * Handle missing values
   * Extract time features

2. **Exploratory Data Analysis**

   * Summary statistics
   * Distribution analysis
   * Time series analysis
   * Variable relationship exploration

3. **Visualization**

   * Histograms
   * Time series plots
   * Scatter plots
   * Seasonal boxplots

---

## Project Structure

```
project-2-water-quality-analysis
│
├── data
│   ├── raw
│   └── processed
│
├── outputs
│   └── figures
│
├── src
│   ├── clean_water_quality.py
│   ├── eda_water_quality.py
│   └── run_pipeline.py
│
├── notebooks
│
├── README.md
└── requirements.txt
```

---

## How to Run the Project

Clone the repository:

```
git clone <repo-url>
```

Activate the environment:

```
conda activate portfolio-week1
```

Run the pipeline:

```
python src/run_pipeline.py
```

---

## Key Outputs

The analysis produces visualisations exploring:

* Dissolved oxygen distribution
* pH distribution
* Water temperature trends over time
* Relationships between water temperature and dissolved oxygen
* Seasonal patterns in water temperature

Figures are saved in:

```
outputs/figures/
```

---

## Tools Used

* Python
* pandas
* matplotlib
* VS Code
* Git / GitHub

---

## Future Improvements

Possible extensions of this analysis include:

* Spatial comparison of monitoring sites
* Seasonal trend decomposition
* Predictive modelling of dissolved oxygen levels
* Integration with additional environmental datasets
