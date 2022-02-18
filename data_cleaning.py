import pandas as pd

# Reading original data file
df = pd.read_csv('covid-variants.csv')

# Removes negative percentage (-0.00)
df.drop(df[(df.perc_sequences < 0)].index, inplace=True)

# Dropping all rows except where variants are Alpha, Beta, Delta, Omicron, or Mu
df = df.drop(df.index[~df.variant.isin(['Alpha', 'Beta', 'Delta', 'Omicron', 'Mu'])])

# Restarting index numbering
df = df.reset_index(drop=True)

# Writing to new cleaned data file
df.to_csv('covid-variants-cleaned.csv')
