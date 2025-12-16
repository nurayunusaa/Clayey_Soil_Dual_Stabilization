import pandas as pd

# Load raw data
ucs = pd.read_csv('../data/raw/UCS_CBR_data.csv')
swelling = pd.read_csv('../data/raw/swelling_data.csv')
props = pd.read_csv('../data/raw/stabilizer_properties.csv')

# Example preprocessing
ucs_processed = ucs[['Material','Replacement','28_Days_MPa','PAI']]
ucs_processed.to_csv('../data/processed/UCS_CBR_processed.csv', index=False)

swelling.to_csv('../data/processed/swelling_processed.csv', index=False)
