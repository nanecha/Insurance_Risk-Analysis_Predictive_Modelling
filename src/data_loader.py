import pandas as pd
import sys
from pathlib import Path 
sys.path.append(str(Path.cwd() / 'src'))


def load_insurance_data(file_path):
    """
    Load the dataset and return a DataFrame.
    """
    df = pd.read_csv(file_path, dtype={32: object, 37: object})
    #print(df.head())
    print("Shape:", df.shape)
    print("Memory Usage (bytes):", df.memory_usage(deep=True).sum())
    return df