import pandas as pd

df = pd.read_csv('Data file/Airbnb_Open_Data.csv')

# clean Item

# unique_val = df['Item'].unique()
# print(unique_val)

print('\n\n')
print(df.isna().sum())
print('\n\n')
print(df.info())
# print(df.describe().round())
