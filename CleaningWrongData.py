import pandas as pd

df = pd.read_excel('product.xlsx')

for x in df.index:
  if df.loc[x, "Price"] > 1200:
    df.drop(x, inplace = True)


print(df.to_string())