from contextlib import suppress
from ftplib import error_reply
from os import replace
from re import S
from statistics import median

import pandas as pd
import numpy as np

# Point to the subfolder where the CSV actually lives
df = pd.read_csv('dirty_cafe_sales/dirty_cafe_sales.csv')

# Remove duplicate values
df = df.drop_duplicates(subset=['id']).reset_index(drop=True)

# lower column name
df.columns = df.columns.str.lower().str.strip().str.replace(' ','_')

# name
df['name'] = df['name'].fillna('Unknown').astype(str).str.title().str.strip()

# host_identity_verified
df['host_identity_verified'] = df['host_identity_verified'].fillna('unconfirmed')

# host name
df['host_name'] =df['host_name'].astype(str).str.title().str.strip()
df['host_name'] = df['host_name'].fillna('no-name')

# neighbourhood_group
df['neighbourhood_group'] = df['neighbourhood_group'].astype(str).str.title().str.strip()
df['neighbourhood_group'] = df['neighbourhood_group'].fillna('Unknown')

# neighbourhood
df['neighbourhood'] = df['neighbourhood'].astype(str).str.title().str.strip()
df['neighbourhood'] = df['neighbourhood'].fillna('unknown')


# lat &  long 
df = df.dropna(subset=['lat', 'long'])


# Country
df['country'] = df['country'].fillna('United States')

#country_code 
df['country_code'] =df['country_code'].fillna('us').str.upper()

# instant_bookable
df['instant_bookable'] =df['instant_bookable'].astype(str)
df['instant_bookable'] =df['instant_bookable'].replace(['nan'],'unknown').fillna('unknown').str.title()

# cancellation_policy
df['cancellation_policy'] =df['cancellation_policy'].replace(['nan'],'unknown').fillna('unknown').str.title()

# construction_year
df['construction_year'] = pd.to_numeric(df['construction_year'],errors='coerce')
df['construction_year'] = df['construction_year'].astype('Int64')
median_year = df['construction_year'].median()
df['construction_year'] = df['construction_year'].fillna(median_year)

# price 
df['price'] = df['price'].astype(str).str.replace('$','',regex=False).str.replace(',','',regex=False).str.strip()
df['price'] =pd.to_numeric(df['price'],errors='coerce')
df['price'] =df['price'].fillna(df['price'].median()).round(2)

# service_fee 
df['service_fee'] = df['service_fee'].astype(str).str.replace('$','',regex=False).str.replace(',','',regex=False).str.strip()
df['service_fee'] = pd.to_numeric(df['service_fee'],errors='coerce')
df['service_fee'] = df['service_fee'].fillna(df['service_fee'].median()).round(2)

# minimum_nights
np.set_printoptions(suppress=True)
df['minimum_nights'] = df['minimum_nights'].abs()
df['minimum_nights'] = pd.to_numeric(df['minimum_nights'],errors='coerce')
df['minimum_nights'] = df['minimum_nights'].astype('Int64')
df.loc[df['minimum_nights'] > 365 ,'minimum_nights'] = 365
df['minimum_nights'] = df['minimum_nights'].fillna(0)

# number_of_reviews
df['number_of_reviews'] = pd.to_numeric(df['number_of_reviews'], errors='coerce')
df['number_of_reviews'] = df['number_of_reviews'].fillna(0)
df['number_of_reviews'] = df['number_of_reviews'].astype('int64')


# last_review
df['last_review'] = pd.to_datetime(df['last_review'],errors='coerce')
df['last_review'] = df['last_review'].dt.strftime('%d-%m-%y')
df['last_review'] = df['last_review'].ffill()

# reviews_per_month
df['reviews_per_month'] = pd.to_numeric(df['reviews_per_month'],errors='coerce')
df['reviews_per_month'] = df['reviews_per_month'].fillna(0).round(2)

# review_rate_number
df['review_rate_number'] = df['review_rate_number'].fillna(0)

# availability_365
df['availability_365'] = df['availability_365'].fillna(0)
df['availability_365'] = pd.to_numeric(df['availability_365'],errors='coerce')
df['availability_365'] = df['availability_365'].abs()
df.loc[df['availability_365'] > 365 ,'availability_365'] = 365

# calculated_host_listings_count
df['calculated_host_listings_count'] = df['calculated_host_listings_count'].fillna(0)
df['calculated_host_listings_count'] = pd.to_numeric(df['calculated_host_listings_count'],errors='coerce')
df['calculated_host_listings_count'] = df['calculated_host_listings_count'].abs()

# house_rules
df['house_rules'] = df['house_rules'].astype(str).str.title().str.strip()
df['house_rules'] = df['house_rules'].fillna('unknown')

# license
df.drop(columns=['license'], inplace=True)

done = df.to_csv('clean_sales_data.csv',index=False)