# Author : --Singghet

import pandas as pd
import csv

dataset = pd.read_csv('flights_dataset.csv')

# 1.pre-review the data_frame

print(dataset.size)                   # check data size
print(dataset.shape)              # check data shape
print(dataset.dtypes)            # check data type


# 2.1 find  missing values for each column

missing_values_count = dataset.isnull().sum()
print(missing_values_count)


# 2.2  split dataset into two subset  for two types of problems.

df_n = dataset.iloc[:, 0:20].dropna()       # generate subset  about normal flights

df_c = dataset[dataset['Cancelled'] == 1]         # generate subset  about cancelled flights
df_c = df_c.iloc[:, 0:21].dropna(axis=1)
