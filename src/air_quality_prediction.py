import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

DATAPATH = '../data/AirQualityUCI.csv'

data = pd.read_csv(DATAPATH, sep=';')


print(data.shape)


# first get rid of all instances where there is an empty value
data.dropna(axis=1, how='all', inplace=True) # delete column with Nan
data.dropna(axis=0, how='all', inplace=True) # delete row with NaN

print(data.shape)

# Data cleaning and feature engineering
data['Date'] = pd.to_datetime(data['Date'])

print(data.iloc[:, 2:])


print(data.head())

for col in data.iloc[:, 2:].columns:
    print(data[col].dtypes)
    if data[col].dtypes == object:
        data[col] = data[col].str.replace(',', '.').astype('float')

def positive_average(num):
    return num[num > -200].mean()

print("-------data------")
print(data)
print("-------data------")
daily_data = data.drop('Time', axis=1)

print("-------dropped data------")
print(daily_data)
print("-------data------")

