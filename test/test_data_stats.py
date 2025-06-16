import unittest
import pandas as pd
import sys
import os
from src.data_stats import generate_descriptive_stats
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(
                'F:/Insurance_Risk-Analysis_Predictive_Modelling/test'
            ),
            '..'
        )
    )
)


class TestDescriptiveStats(unittest.TestCase):
    def setUp(self):
        """Create a sample DataFrame for testing."""
        self.df = pd.DataFrame({
            'TotalPremium': [100, 200, 300, 400, 500],
            'SumInsured': [10000, 20000, 30000, 40000, 50000],
            'kilowatts': [80, 90, 100, 110, 120],
            # Test non-numeric exclusion
            'NonNumeric': ['A', 'B', 'C', 'D', 'E']
        })

    def test_default_columns(self):
        """Test with default numerical columns."""
        stats = generate_descriptive_stats(self.df)
        self.assertIn('TotalPremium', stats.columns)
        self.assertIn('SumInsured', stats.columns)
        self.assertEqual(stats.shape[0], 8)  # 8 stats (count, mean, std, etc.)

    def test_custom_columns(self):
        """Test with custom column list."""
        custom_cols = ['SumInsured', 'kilowatts']
        stats = generate_descriptive_stats(self.df, numerical_cols=custom_cols)
        self.assertIn('kilowatts', stats.columns)
        # Only 'kilowatts' exists (misspelled 'SumInsured')
        self.assertEqual(stats.shape[1], 1)

    def test_missing_columns(self):
        """Test with non-existent columns."""
        stats = generate_descriptive_stats(
            self.df, numerical_cols=['MissingColumn'])
        self.assertIsNone(stats)  # Should return None

    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        empty_df = pd.DataFrame()
        stats = generate_descriptive_stats(empty_df)
        self.assertIsNone(stats)


if __name__ == '__main__':
    unittest.main()
