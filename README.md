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

Key Findings
1. Strong Negative Relationship Between Temperature and Dissolved Oxygen
A clear inverse relationship was identified between water temperature and dissolved oxygen levels.
The regression model estimates that:
A 1°C increase in water temperature is associated with a ~0.18 mg/L decrease in dissolved oxygen.
This aligns with established physical principles, as warmer water holds less dissolved oxygen, increasing the risk of ecological stress during warmer periods.
2. Multi-Factor Influence on Water Quality
Expanding the model to include additional environmental variables revealed that dissolved oxygen is influenced by multiple interacting factors, not temperature alone.
Key relationships identified:
Salinity shows a positive association with dissolved oxygen in this dataset.
pH is positively related to dissolved oxygen, potentially reflecting biological activity such as photosynthesis.
Water depth also exhibits a positive relationship, suggesting possible effects of mixing or site-specific hydrological conditions.
These findings highlight the complex and system-based nature of aquatic environments.
3. Model Performance and Predictive Power
A simple linear model using only temperature achieved:
R² ≈ 0.20
Mean Absolute Error ≈ 1.73 mg/L
After incorporating additional predictors (salinity, pH, and water depth), performance improved to:
R² ≈ 0.27
Mean Absolute Error ≈ 1.59 mg/L
This demonstrates that including multiple environmental variables improves predictive performance, though the model still explains only a portion of the total variability.
4. Limitations and Model Interpretation
Despite improvements, the model explains only ~27% of the variance in dissolved oxygen.
This suggests that:
Additional factors (e.g. biological activity, nutrient levels, seasonal dynamics) likely play a significant role.
Linear regression may not fully capture the complexity of environmental processes.
The model should therefore be interpreted as providing directional insights rather than precise predictions.
5. Environmental Implications
The results reinforce the importance of temperature as a key driver of water quality, particularly under changing climate conditions.
The multi-variable model highlights that management decisions should consider multiple environmental indicators, rather than relying on a single metric.
This approach can support:
early identification of ecological stress conditions
improved monitoring strategies
more informed environmental decision-making