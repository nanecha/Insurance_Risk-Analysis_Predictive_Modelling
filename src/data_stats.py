import pandas as pd
from tabulate import tabulate


def generate_descriptive_stats(df, numerical_cols=None):
    # Default columns if none provided
    if numerical_cols is None:
        numerical_cols = [
            'TotalPremium', 'TotalClaims', 'SumInsured', 'CustomValueEstimate',
            'Cylinders', 'cubiccapacity', 'kilowatts', 'NumberOfDoors'
        ]

    # Filter to columns that exist in the DataFrame
    available_cols = [col for col in numerical_cols if col in df.columns]

    if not available_cols:
        print("⚠️ Warning: None of the specified numerical columns exist "
              "in the DataFrame.")
        return None

    # Generate and print stats
    print("\n=== Descriptive Statistics ===")
    stats = df[available_cols].describe()

    return stats


def missing_values(df):

    print("\n=== Missing Values ===")
    missingvalues = df.isnull().sum()
    print(missingvalues[missingvalues > 0])
    # Check for duplicates
    print("Number of duplicates:", df.duplicated().sum())
    return missingvalues


def calculate_claim_premium_summary(df):
    total_claim = df['TotalClaims'].sum()
    total_premium = df['TotalPremium'].sum()
    loss_ratio = total_claim / \
        total_premium if total_premium != 0 else float('nan')
    summary = pd.DataFrame({
        'Metric': ['Total Claims', 'Total Premium', 'Overall Loss Ratio'],
        'Value': [total_claim, total_premium, loss_ratio],
        'Formatted': [
            f"{total_claim:,.0f}",
            f"{total_premium:,.0f}",
            f"{loss_ratio:.2%}" if total_premium != 0 else "N/A"
        ]
    })
    print("Key calculation over same Important column ")
    print("===================================================")
    print(summary)
    return summary
# This code calculates and displays the insurance loss ratio


def calculate_and_display_loss_ratios(df):
    # Calculate loss ratios by different categories
    loss_ratio_by_province = df.groupby('Province').apply(
        lambda x: x['TotalClaims'].sum(
        ) / x['TotalPremium'].sum() if x['TotalPremium'].sum() != 0 else 0,
        include_groups=False
    ).reset_index(name='LossRatio')

    loss_ratio_by_vehicle = df.groupby('VehicleType').apply(
        lambda x: x['TotalClaims'].sum(
        ) / x['TotalPremium'].sum() if x['TotalPremium'].sum() != 0 else 0,
        include_groups=False
    ).reset_index(name='LossRatio')

    loss_ratio_by_gender = df.groupby('Gender').apply(
        lambda x: x['TotalClaims'].sum(
        ) / x['TotalPremium'].sum() if x['TotalPremium'].sum() != 0 else 0,
        include_groups=False
    ).reset_index(name='LossRatio')

    # Prepare table data
    table_data = []
    table_data.extend([["Province", row['Province'], f"{row['LossRatio']:.2f}"]
                      for _, row in loss_ratio_by_province.iterrows()])
    table_data.extend([
        ["VehicleType", row['VehicleType'], f"{row['LossRatio']:.2f}"]
        for _, row in loss_ratio_by_vehicle.iterrows()
    ])
    table_data.extend([["Gender", row['Gender'], f"{row['LossRatio']:.2f}"]
                      for _, row in loss_ratio_by_gender.iterrows()])

    # Define headers for the table
    headers = ["Category", "Value", "Loss Ratio"]

    # Print tabulated output
    print("\n=== Loss Ratios by Province, VehicleType, and Gender ===")
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

    # Display Loss Ratio by Gender
    print("\n=== Loss Ratio by Gender ===")
    print(loss_ratio_by_gender.to_string(index=False))

# Example usage:
# calculate_and_display_loss_ratios(your_dataframe)
