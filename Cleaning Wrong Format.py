import pandas as pd

df = pd.read_excel('website access history.xlsx')

df['AccessDate'] = pd.to_datetime(df['AccessDate'])

df.dropna(subset=['AccessDate'], inplace = True)

print(df.to_string())