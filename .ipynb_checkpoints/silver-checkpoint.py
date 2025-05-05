"""
Purpose:
- Loads bronze-layer data from 'starB.csv'.
- Converts to silver-layer DataFrame (dfS) with standardized column names.
- Output: Cleaned DataFrame ready for silver-layer processing.
"""

# =============================================================================
# Importing Libraries
# =============================================================================
import pandas as pd
from pathlib import Path

# =============================================================================
# Load Bronze Data
# =============================================================================
# Set absolute paths
notebook_path = Path().absolute()
project_root = notebook_path.parent
bronze_path = project_root / 'data' / 'bronze' / 'starB.csv'

# Load CSV
dfB = pd.read_csv(bronze_path)

# =============================================================================
# Create Silver DataFrame
# =============================================================================
# Create copy and rename columns
dfS = dfB.rename(columns={
    # Your exact specified columns
    'recno': 'recno',
    'Class': 'type',
    'subCl': 'full_class',
    'SpT': 'spt',
    'Teff1': 'effective_temperature_1',
    'e_Teff1': 'effective_temperature_error_1',
    'logg1': 'log_surface_gravity_1',
    'e_logg1': 'log_surface_gravity_error_1',
    'FeH1': 'metallicity_fe_h_1',
    'e_FeH1': 'metallicity_fe_h_error_1',
    'Vmag': 'visual_magnitude',
    'Teff2': 'effective_temperature_2',
    'logg2': 'log_surface_gravity_2',
    'FeH2': 'metallicity_fe_h_2',
    'Rad': 'radius',
    'Mass': 'mass',
    'Lum': 'luminosity',
    'Dist': 'distance',
    
    # All other columns converted to snake_case
    'Version': 'version',
    'FileName': 'file_name',
    'EB': 'eb',
    'LAMOST': 'lamost',
    'Bin': 'bin',
    'RAJ2000': 'ra_j2000',
    'DEJ2000': 'de_j2000',
    'Date': 'date',
    'SNg': 's_ng',
    'SepTESS': 'sep_tess',
    'e_Vmag': 'visual_magnitude_error',
    'Flag': 'flag',
    's_Teff2': 'teff_2_sigma',
    's_logg2': 'logg_2_sigma',
    'e_FeH2': 'fe_h_2_error',
    's_Rad': 'radius_sigma',
    's_Mass': 'mass_sigma',
    's_Lum': 'luminosity_sigma',
    's_Dist': 'distance_sigma',
    'DR7': 'dr7'
})

# Filter columns
keep_columns = [
    'lamost', 'date' ,
    'recno', 'full_class', 'spt',
    'effective_temperature_1', 'effective_temperature_error_1',
    'log_surface_gravity_1', 'log_surface_gravity_error_1',
    'metallicity_fe_h_1', 'metallicity_fe_h_error_1',
    'visual_magnitude',
    'effective_temperature_2', 'log_surface_gravity_2', 'metallicity_fe_h_2',
    'radius', 'mass', 'luminosity', 'distance'
]
dfS = dfS[keep_columns]

# =============================================================================
# Save Silver Data 
# =============================================================================
silver_path = project_root / 'data' / 'silver' / 'starS.csv'
dfS.to_csv(silver_path, index=False)
dfS