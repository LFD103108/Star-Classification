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
    'subClass': 'full_class',
    'SpT': 'spt',
    'Teff': 'effective_temperature',
    'e_Teff': 'effective_temperature_error',
    'logg': 'log_surface_gravity',
    'e_logg': 'log_surface_gravity_error',
    '[Fe/H]': 'metallicity_fe_h',
    'e_[Fe/H]': 'metallicity_fe_h_error',
    'Vmag': 'visual_magnitude',
    'Rad': 'radius',
    'Mass': 'mass',
    'Lum': 'luminosity',
    'Dist': 'distance',
    
    # All other columns converted to snake_case
    'ObsID': 'observation_id',
    'Target': 'target_name',
    'Obs_Date': 'observation_date',
    'LMJD': 'local_mjd',
    'MJD': 'modified_julian_date',
    'PlanId': 'plan_id',
    'spId': 'spectrum_id',
    'FiberId': 'fiber_id',
    'RAJ2000': 'ra_j2000',
    'DEJ2000': 'de_j2000',
    'snru': 'signal_to_noise_u',
    'snrg': 'signal_to_noise_g',
    'snrr': 'signal_to_noise_r',
    'snri': 'signal_to_noise_i',
    'snrz': 'signal_to_noise_z',
    'objType': 'object_type',
    'z': 'redshift',
    'e_z': 'redshift_error',
    'magType': 'magnitude_type',
    'mag1': 'magnitude_u',
    'mag2': 'magnitude_g',
    'mag3': 'magnitude_r',
    'mag4': 'magnitude_i',
    'mag5': 'magnitude_z',
    'mag6': 'magnitude_j',
    'mag7': 'magnitude_h',
    'tsource': 'target_source',
    'FiberType': 'fiber_type',
    'tfrom': 'target_origin',
    'tcomment': 'target_comment',
    'offsets': 'position_offset',
    'offsetsv': 'velocity_offset',
    'RAOdeg': 'observed_ra_deg',
    'DEOdeg': 'observed_dec_deg',
    'RV': 'radial_velocity',
    'e_RV': 'radial_velocity_error',
    'GaiaDR2': 'gaia_dr2_id',
    'Gmag': 'gaia_g_magnitude'
})


# =============================================================================
# Save Silver Data 
# =============================================================================
silver_path = project_root / 'data' / 'silver' / 'starS.csv'
dfS.to_csv(silver_path, index=False)
dfS