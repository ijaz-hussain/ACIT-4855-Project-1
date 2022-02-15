import pandas as pd

df = pd.read_csv('covid-variants.csv')
df.drop(df.index[~df.variant.isin(['Alpha', 'Beta', 'Delta', 'Omicron', 'Mu'])])
df.drop(columns=df.columns[0], axis=1, inplace=True)
df.to_csv('covid-variants-cleaned.csv')
