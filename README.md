# Disparities in Air Pollution Exposure (Texas)

This project analyzes disparities in PM2.5 exposure across Texas ZIP Code Tabulation Areas (ZCTAs) using
demographic, traffic, and environmental data.

## Research Question
How do traffic intensity and socioeconomic characteristics relate to PM2.5 exposure across communities in Texas?

## Data
- ACS (2011–2021): race, income, education
- Traffic volume and intersection density
- PM2.5 concentrations (target variable)

## Methods
- Data preprocessing and ZCTA-level merging
- Correlation analysis of traffic metrics
- Linear Regression, Lasso, Random Forest, XGBoost
- PCA and Scikit-learn Pipelines
- Hyperparameter tuning with GridSearchCV

## Key Findings
- Traffic metrics are highly correlated; selected representative variables
- Random Forest Regression achieved the best performance (~0.80 R²)
- Socioeconomic and demographic variables show differentiated associations with PM2.5

## Repository Structure
See `/src` for reusable modeling code and `/slides` for the final presentation.

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
