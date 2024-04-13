import pandas as pd

df = pd.read_excel('product trending.xlsx')

df.drop_duplicates(inplace = True)

print(df.to_string())