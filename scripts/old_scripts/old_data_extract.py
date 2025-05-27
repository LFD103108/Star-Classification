"""
Purpose:
- Extracts stellar data from VizieR catalog "J/ApJS/266/14" via TAP query.
- Saves raw data to `/data/bronze/starB.csv` without intermediate DataFrame storage.
- Avoids visualizations; focuses on data extraction and storage.
"""

# =============================================================================
# Importing Libraries
# =============================================================================
from pyvo import registry  # Access astronomical databases (VizieR, TAP services)
from pathlib import Path  # Cross-platform filesystem path handling

# =============================================================================
# Query Setup & Execution
# =============================================================================
CATALOGUE = "J/ApJS/266/14"  # Target VizieR catalog
catalogue_ivoid = f"ivo://CDS.VizieR/{CATALOGUE}"  # Construct IVOA identifier

# Fetch catalog metadata and table list
voresource = registry.search(ivoid=catalogue_ivoid)[0]
tables = voresource.get_tables()
first_table_name = list(tables.keys())[0]  # Get first table name dynamically

# Execute TAP query to extract ALL columns (no explicit column selection)
tap_service = voresource.get_service("tap")
tap_records = tap_service.search(f'SELECT * FROM "{first_table_name}"')

# =============================================================================
# Data Storage
# =============================================================================
# Save directly to CSV without DataFrame variable
tap_records.to_table().to_pandas().to_csv(
    Path(__file__).parent.parent / 'data' / 'bronze' / 'starB.csv',
    index=False
)

# Table and Schema
#print( tap_records.to_table() )