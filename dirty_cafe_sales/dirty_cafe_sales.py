import pandas as pd

df = pd.read_csv('Airbnb_Open_Data.csv')

# remove duplicate value
df = df.drop_duplicates(subset=['id']).reset_index(drop=True)



print('\n\n')
print(df.isna().sum())

