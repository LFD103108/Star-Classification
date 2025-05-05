"""
Purpose:
- Processes silver-layer data (starS.csv) into gold-layer format
- Converts dates, splits spectral classes, creates composite keys
- Output: Cleaned DataFrame saved to /data/gold/starG.csv
"""

# =============================================================================
# Importing Libraries
# =============================================================================
import pandas as pd
from pathlib import Path

# =============================================================================
# Path Configuration
# =============================================================================
project_root = Path().absolute().parent
silver_path = project_root / 'data' / 'silver' / 'starS.csv'
gold_path = project_root / 'data' / 'gold'
gold_path.mkdir(parents=True, exist_ok=True)

# =============================================================================
# Data Processing
# =============================================================================
# Load silver data
dfG = pd.read_csv(silver_path)

# Convert timestamp
dfG['date'] = pd.to_datetime(dfG['date'], unit='s')

# Split spectral classes
dfG[['class', 'subclass', 'luminosity_class']] = dfG['full_class'].str.extract(r'^([A-Za-z]+)(\d+)?([IV]+)?$')
dfG['subclass'] = [str(dfG['class'][j])+ str(dfG['subclass'][j]) for j in range(len(dfG))]
dfG['luminosity_class'] = dfG['luminosity_class'].fillna('')

# Create composite key
dfG['identifier'] = dfG['date'].dt.strftime('%Y%m%d') + '_' + dfG['lamost'].astype(str)

# =============================================================================
# Column Reordering
# =============================================================================
other_columns = [col for col in dfG.columns 
                if col not in ['identifier', 'class', 'subclass', 
                              'luminosity_class', 'full_class', 'lamost', 'date']]

dfG = dfG[['identifier', 'class', 'subclass', 'luminosity_class', 'full_class'] + 
          other_columns + 
          ['lamost', 'date']]

# =============================================================================
# Data Export
# =============================================================================
dfG.to_csv(gold_path / 'starG.csv', index=False)