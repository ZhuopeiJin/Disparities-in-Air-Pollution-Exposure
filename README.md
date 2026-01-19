# Disparities in Air Pollution Exposure (Texas)

This project investigates disparities in PM2.5 air pollution exposure across
Texas ZIP Code Tabulation Areas (ZCTAs) by integrating environmental,
traffic, and socioeconomic data. The analysis focuses on how traffic
intensity and demographic characteristics relate to PM2.5 concentrations.

The project was completed as part of a graduate-level data science course
and emphasizes a transparent, reproducible, notebook-based workflow.

---

## Research Question

How do traffic conditions and socioeconomic characteristics relate to
PM2.5 exposure across communities in Texas?

---

## Data Sources

- **PM2.5 Concentrations**  
  ZCTA-level PM2.5 estimates used as the target variable.

- **American Community Survey (ACS, 2011–2021)**  
  Demographic and socioeconomic variables including race, income,
  population density, and educational attainment.

- **Traffic Data**  
  Intersection-level traffic volume and derived traffic intensity measures.

> Due to data size and licensing constraints, full raw datasets are not
> included in this repository. Sample files and data schemas are provided
> for reproducibility.

---

## Methodology

1. Data preprocessing and cleaning  
   - Removal of missing values  
   - Harmonization of ZCTA and year identifiers  
   - Merging environmental, traffic, and ACS datasets  

2. Exploratory data analysis  
   - Correlation analysis of traffic variables  
   - Feature selection based on multicollinearity  

3. Modeling approaches  
   - Linear Regression  
   - Lasso Regression  
   - Random Forest Regression  
   - Gradient Boosting Regression  
   - XGBoost (optional)  

4. Dimensionality reduction and pipelines  
   - Principal Component Analysis (PCA)  
   - Scikit-learn pipelines and GridSearchCV for model tuning  

---

## Key Findings

- Traffic variables exhibit high multicollinearity; representative metrics
  were selected for modeling.
- Tree-based models outperform linear and regularized regression approaches.
- Random Forest Regression achieved the strongest predictive performance
  (approximately R² ≈ 0.80 on the test set).
- Socioeconomic and demographic variables show differentiated associations
  with PM2.5 exposure across Texas ZCTAs.

---

## Repository Structure

```text
disparities-air-pollution/
├── notebooks/
│   └── analysis.ipynb        # Main analysis notebook (run this)
├── src/
│   ├── load_data.py          # Data loading utilities
│   ├── preprocess.py         # Data cleaning and merging functions
│   ├── models.py             # Regression and ML models
│   └── pipeline.py           # Pipelines and hyperparameter tuning
├── data/
│   ├── raw/                  # Raw data (not fully included)
│   └── README.md             # Data descriptions and sources
├── slides/
│   └── Disparities_Air_Pollution.pdf
├── requirements.txt
└── README.md
