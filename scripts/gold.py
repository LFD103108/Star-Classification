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
from astropy.time import Time

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

# Filter columns
keep_columns = [
     'observation_id', 'observation_date', 'full_class',
     'effective_temperature', 'log_surface_gravity','metallicity_fe_h', 
     'radial_velocity', 'redshift' 
      #'magnitude_type', 'magnitude_u', 'magnitude_g',
      # 'magnitude_r', 'magnitude_i', 'magnitude_z', 'magnitude_j',
      #'magnitude_h'
 ]
dfG = dfG[keep_columns]

# Organizing the columns
dfG.insert(0, 'identifier', dfG['observation_id'].astype(str) + dfG['observation_date']) # creates a composite hard key 'observation_id' + 'observation_date'
dfG.insert(3, 'class', dfG['full_class'].str[0])                                               # inserts the 'class' column, useful for later training

# =============================================================================
# Data Export
# =============================================================================
dfG.to_csv(gold_path / 'starG.csv', index=False)