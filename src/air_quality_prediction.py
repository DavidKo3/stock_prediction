import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

DATAPATH = '../data/AirQualityUCI.csv'

data = pd.read_csv(DATAPATH, sep=';')
print(data.head())

print(data.shape)


# first get rid of all instances where there is an empty value
data.dropna(axis=1, how='all', inplace=True)
data.dropna(axis=0, how='all', inplace=True)

print(data.shape)

# Data cleaning and feature engineering
data['Date'] = pd.to_datetime(data['Date'])

print(data.iloc[:, 2:])
