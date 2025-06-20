# Task 4: Predictive Modeling Report

## Claim Severity Results
| Model             |    RMSE |       R² |
|-------------------|---------|----------|
| Linear Regression | 33733.4 | 0.292435 |
| Random Forest     | 34910.2 | 0.242204 |
| XGBoost           | 37746.6 | 0.114064 |
## Premium Prediction Results
| Model         |    RMSE |       R² |
|---------------|---------|----------|
| Random Forest | 41.7195 | 0.978197 |
| XGBoost       | 37.3255 | 0.982548 |
## Claim Probability Results
| Model         |   Accuracy |   Precision |     Recall |   F1-Score |
|---------------|------------|-------------|------------|------------|
| Random Forest |   0.997215 |           1 | 0.00179211 | 0.00357782 |
| XGBoost       |   0.99721  |           0 | 0          | 0          |
## Top 5 Features (SHAP)
- VehicleAge: Increases claim by ~2000 Rand per year older
- SumInsured: Increases claim by ~1.5 Rand per 1000 Rand insured
- IsHighRiskProvince: Increases claim by ~5000 Rand in high-risk provinces
- VehicleType_Heavy Commercial: Increases claim by ~10000 Rand vs. Passenger
- PremiumToSumInsuredRatio: Lower ratios increase claim by ~3000 Rand

## Business Implications
- **VehicleAge**: Raise premiums for older vehicles to cover higher claims.
- **SumInsured**: Scale premiums with insured amounts.
- **IsHighRiskProvince**: Apply surcharges in high-risk provinces (e.g., Gauteng).
- **VehicleType**: Higher rates for commercial vehicles.
- **PremiumToSumInsuredRatio**: Avoid underpricing to reduce claim exposure.
