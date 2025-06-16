import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd


def plot_numerical_distributions(
    df,
    numerical_cols=None,
    color_palette="husl",
    figsize=(12, 8)
):

    # Set default columns if none provided
    if numerical_cols is None:
        numerical_cols = ['TotalPremium', 'TotalClaims', 'CustomValueEstimate']

    # Set style and colors
    sns.set(style="whitegrid")
    colors = sns.color_palette(color_palette, len(numerical_cols))

    # Create figure
    plt.figure(figsize=figsize)

    # Plot each numerical column
    for i, col in enumerate(numerical_cols, 1):
        plt.subplot(2, 2, i)
        sns.histplot(df[col], kde=True, bins=30, color=colors[i - 1])
        plt.title(f'Distribution of {col}', fontsize=13)
        plt.xlabel(col, fontsize=11)
        plt.ylabel("Frequency", fontsize=11)
        plt.grid(True, linestyle='--', alpha=0.6)

    # Add main title and adjust layout
    plt.suptitle("Numerical Feature Distributions",
                 fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def plot_categorical_distributions(
    df,
    categorical_cols=None,
    figsize=(10, 4),
    rotation=45,
    save_path=None,
    palette='husl'
):
    # Set default columns if none provided
    if categorical_cols is None:
        categorical_cols = ['Province', 'VehicleType', 'Gender']

    # Set style
    sns.set(style="whitegrid")

    for col in categorical_cols:
        plt.figure(figsize=figsize)

        # Create ordered value counts
        value_counts = df[col].value_counts()

        # Plot with seaborn for better aesthetics
        ax = sns.barplot(x=value_counts.index,
                         y=value_counts.values,
                         palette=palette)

        # Add counts on top of bars
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 5),
                        textcoords='offset points')

        plt.title(f'Distribution of {col}', fontsize=14, pad=20)
        plt.xlabel(col, fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=rotation)
        plt.tight_layout()

        # Save figure if path provided
        if save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            plt.savefig(f'{save_path}/{col}_distribution.png',
                        dpi=300, bbox_inches='tight')

        plt.show()


def plot_outliers_boxplot(
    df,
    numerical_cols=None,
    figsize=(12, 6),
    palette="Set2",
    showfliers=True,
    whis=1.5,
    save_path=None
):

    # Set default columns if none provided
    if numerical_cols is None:
        numerical_cols = ['TotalPremium', 'TotalClaims']

    # Set style and colors
    sns.set(style="whitegrid")
    colors = sns.color_palette(palette, len(numerical_cols))

    # Create figure
    plt.figure(figsize=figsize)

    # Plot each numerical column
    for i, col in enumerate(numerical_cols, 1):
        plt.subplot(1, len(numerical_cols), i)
        sns.boxplot(y=df[col], color=colors[i - 1],
                    showfliers=showfliers, whis=whis)

        # Calculate and display outlier count
        if showfliers:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - whis * iqr
            upper_bound = q3 + whis * iqr
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            plt.annotate(
                f'Outliers: {len(outliers)}\n'
                f'({len(outliers)/len(df)*100:.1f}%)',
                xy=(0.05, 0.95),
                xycoords='axes fraction',
                ha='left',
                va='top',
                bbox=dict(boxstyle='round', fc='white')
            )

        plt.title(f'Box Plot of {col}', fontsize=14)
        plt.ylabel(col, fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)

    plt.suptitle("Outlier Detection in Numerical Features",
                 fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save figure if path provided
    if save_path:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(f'{save_path}/outlier_detection.png',
                    dpi=300, bbox_inches='tight')

    plt.show()

    # boxplot


def plot_correlation_matrix(
    df,
    numerical_cols=None,
    figsize=(10, 8),
    cmap='coolwarm',
    annot=True,
    fmt=".2f",
    title=None,
    save_path=None,
    mask_upper=False,
    **heatmap_kws
):

    # Set default columns if none provided
    if numerical_cols is None:
        numerical_cols = ['TotalPremium', 'TotalClaims',
                          'SumInsured', 'CustomValueEstimate']

    # Calculate correlation matrix
    corr_matrix = df[numerical_cols].corr()

    # Create mask if needed
    mask = None
    if mask_upper:
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Create figure
    plt.figure(figsize=figsize)

    # Plot heatmap
    sns.heatmap(corr_matrix,
                annot=annot,
                fmt=fmt,
                cmap=cmap,
                center=0,
                vmin=-1,
                vmax=1,
                mask=mask,
                square=True,
                linewidths=.5,
                cbar_kws={"shrink": 0.8},
                **heatmap_kws)

    # Set title
    if title is None:
        title = 'Correlation Matrix of Financial Variables' if len(
            numerical_cols) <= 5 else 'Correlation Matrix'
    plt.title(title, fontsize=14, pad=20)

    # Adjust layout
    plt.tight_layout()

    # Save figure if path provided
    if save_path:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(f'{save_path}/correlation_matrix.png',
                    dpi=300,
                    bbox_inches='tight',
                    transparent=True)

    plt.show()


def plot_temporal_trends(
    df,
    date_col='TransactionMonth',
    value_cols=None,
    avg_cols=None,
    figsize=(12, 6),
    colors=None,
    title=None,
    save_path=None,
    rotation=45,
    ylabel1=None,
    ylabel2=None,
    legend_loc='upper center'
):
    """
    Plot temporal trends of insurance metrics with dual y-axes.

    Parameters:
    - df: pandas DataFrame
    - date_col: name of datetime column (default: 'TransactionMonth')
    - value_cols: tuple of (claims_col, premium_col) (default: None)
    - avg_cols: tuple of (avg_claims_col, avg_premium_col) (default: None)
    - figsize: figure size (default: (12, 6))
    - colors: tuple of (claims_color, premium_color) (default: ('red', 'blue'))
    - title: plot title (default: automatic)
    - save_path: directory to save plot (default: None)
    - rotation: x-tick label rotation (default: 45)
    - ylabel1: left y-axis label (default: 'Average Claims')
    - ylabel2: right y-axis label (default: 'Average Premium')
    - legend_loc: legend location (default: 'upper center')
    """
    # Set default values
    if colors is None:
        colors = ('red', 'blue')
    if value_cols is None and avg_cols is None:
        value_cols = ('TotalClaims', 'TotalPremium')

    # Convert to datetime if needed
    if not pd.api.types.is_datetime64_any_dtype(df[date_col]):
        df[date_col] = pd.to_datetime(df[date_col])

    # Group by month if needed
    if avg_cols is None:
        monthly_trends = df.groupby(df[date_col].dt.to_period('M')).agg({
            value_cols[0]: 'mean',
            value_cols[1]: 'mean'
        }).reset_index()
        monthly_trends[date_col] = monthly_trends[date_col].dt.to_timestamp()
        claims_col, premium_col = value_cols[0], value_cols[1]
    else:
        monthly_trends = df.copy()
        claims_col, premium_col = avg_cols[0], avg_cols[1]

    # Create figure
    fig, ax1 = plt.subplots(figsize=figsize)

    # Plot claims
    ax1.plot(monthly_trends[date_col], monthly_trends[claims_col],
             label='Claims', color=colors[0], linewidth=2)
    plt.setp(ax1.get_xticklabels(), rotation=rotation)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(ylabel1 or 'Average Claims', color=colors[0])
    ax1.tick_params(axis='y', labelcolor=colors[0])

    # Create twin axis for premiums
    ax2 = ax1.twinx()
    ax2.plot(monthly_trends[date_col], monthly_trends[premium_col],
             label='Premiums', color=colors[1], linewidth=2)
    ax2.set_ylabel(ylabel2 or 'Average Premium', color=colors[1])
    ax2.tick_params(axis='y', labelcolor=colors[1])

    # Set title
    if title is None:
        title = 'Temporal Trends: Claims vs Premiums'
    plt.title(title, pad=20)

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(lines1 + lines2, labels1 + labels2,
               loc=legend_loc, bbox_to_anchor=(0.5, -0.1), ncol=2)

    plt.tight_layout()

    # Save figure if path provided
    if save_path:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(f'{save_path}/temporal_trends.png',
                    dpi=300,
                    bbox_inches='tight')

    plt.show()
