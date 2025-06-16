
# 📊 Insurance Data Analytics - Exploratory Data Analysis (EDA)
## 🎯 Goal
To develop a foundational understanding of the insurance dataset, assess its quality, and uncover patterns in risk and profitability.

![Python](https://img.shields.io/badge/python-3.9+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-1.3+-%23150458?style=for-the-badge&logo=pandas&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-2.0+-%2313ADC7?style=for-the-badge&logo=dataversioncontrol&logoColor=white)
![CI/CD](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
 
## 📂 Project Structure

│Insurance_Risk-Analysis_Predictive_Modelling/
 ├── .github/workflows/
 │ └── main.yml │              # GitHub Actions CI/CD
 ├── .vscode/
 │ └── settings.json│         # IDE configuration
 ├── .dvc/                    # Data version control
 ├── .venv/                   # Virtual environment
 ├── data/
 │ ├── outputs.csv            # Processed data
 │ └── raw.txt                # Raw datasets
 ├── notebooks/
 │ └── insurance_analysis_eda.ipynb # Exploratory analysis
 ├── src/                      # Python modules
 │ ├── init.py
 │ ├── data_loader.py          # Data ingestion
 │ ├── data_stats.py           # Statistical analysis
 │ └── data_visualization.py   # Plotting utilities
 ├── tests/
 │ ├── init.py
 │ └── test_data_stats.py      # Unit tests
 ├── README.md                 # This file
 ├── requirements.txt          # Dependencies
 └── .gitignore           # Version control exclusions
## 🛠️ Setup & Installation

Load necessary Python packages and configure the notebook for data profiling and EDA. using 'requirements.txt'
git clone https://github.com/nanecha/Insurance_Risk-Analysis_Predictive_Modelling.git
pip install -r requirements.txt

## 1. 📋 Data Understanding and Summarization
The dataset is given in the txt format and converted to CSV file and stored in the data older. This is loaded from `output2.csv` with 1,000,098 rows and 52 columns, including `UnderwrittenCoverID`, `PolicyID`, `TotalPremium`, `TotalClaims`, etc. Memory usage is approximately 390.1 MB.

---
## 2. 📈 Basic Statistical Summarization
- **Data Types**: 1 boolean, 11 floats, 4 integers, 36 objects.
- **Descriptive Statistics**: Key numerical columns (`TotalPremium`, `TotalClaims`, `SumInsured`, etc.) show:
  - `TotalPremium`: Mean ~61.91, Max ~65,282.60
  - `TotalClaims`: Mean ~64.86, Max ~393,092.10
  - `SumInsured`: Mean ~604,172.70, Max ~12,636,200

---

## 3. 🕵️ Data Quality Assessment
- **Missing Values**: Significant in `NumberOfVehiclesInFleet` (100%), `CrossBorder` (~99.9%), `CustomValueEstimate` (~78%).
- **Duplicates**: None found.

---

## 4. 🔢 Key Column Calculations
- **Total Claims**: ~64.87M
- **Total Premium**: ~61.91M
- **Overall Loss Ratio**: 104.77% (TotalClaims / TotalPremium)

---

## 5. 📊 Loss Ratio by Province, Vehicle Type, and Gender
- **By Province**: Gauteng (1.22), KwaZulu-Natal (1.08), Western Cape (1.06).
- **By Vehicle Type**: Heavy Commercial (1.63), Passenger Vehicle (1.05), Bus (0.14).
- **By Gender**: Not specified (1.06), Male (0.88), Female (0.82).

---

## 6. 📉 Univariate Analysis
- **Numerical Distributions**: Visualized for `TotalPremium`, `TotalClaims`, `CustomValueEstimate`.
- **Categorical Distributions**: Analyzed for `Province` and `VehicleType`.
- **Outlier Detection**: Box plots for `TotalPremium`, `TotalClaims`, `CustomValueEstimate` with strict outlier detection (whis=2.0).

---

## 7. 🔗 Bivariate Analysis
- **Correlation Matrix**: Heatmap of financial variables (`TotalPremium`, `TotalClaims`, `SumInsured`, `CustomValueEstimate`).
- **Scatterplot**: `TotalPremium` vs. `TotalClaims` colored by `PostalCode`.

---

## 8. 📅 Temporal Trends
- **Claims and Premiums Over Time**: Monthly trends show increasing averages from 2013-10 to 2015-08.
- **Claim Frequency and Severity**: Calculated using `RegistrationYear` (noted issue with 'M' deprecated in `resample`).

---

## 9. 🚗 Vehicle Make/Model Analysis
- **High Claim Vehicles**: Toyota Quantum models dominate (e.g., 2.7 SESFIKILE 16s: ~12.04M claims).
- **Low Claim Vehicles**: Models like Chevrolet Optra 1.6 L and Mercedes-Benz C200K CLASSIC A/T have minimal or negative claims.

---

## 10. 📊 Visualizations
- **Loss Ratio by Province**: Bar plot showing highest ratios in Gauteng.
- **Loss Ratio by Province and Vehicle Type**: Heatmap with annotations.
- **Temporal Trends**: Dual-axis plot of average claims (red) and premiums (blue).
- **Vehicle Make/Model Performance**: Interactive bubble chart with `AvgClaim`, `LossRatio`, and `PolicyID`.
- **Top Vehicle Makes by Claims**: Bar plot of top 10 makes by total claim amounts.

---

## 11. 💾 Save Results
Results saved to `F:/Insurance_Risk-Analysis_Predictive_Modelling/data/eda_summary.txt`, including overall loss ratio and breakdowns by province, vehicle type, and gender.

---

## 📝 Notes
- Significant missing data in `CustomValueEstimate`, `NumberOfVehiclesInFleet`, and `CrossBorder`.
- Visualizations saved in `F:/Insurance_Risk-Analysis_Predictive_Modelling/data/outputs/`.
