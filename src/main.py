import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from scipy.optimize import minimize
import statsmodels.tsa.api as smt
import statsmodels.api as sm

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

from tqdm import tqdm_notebook
from itertools import product


import warnings
warnings.filterwarnings('ignore')



DATAPATH = '../data/stock_prices_sample.csv'

data = pd.read_csv(DATAPATH, index_col=['DATE'], parse_dates=['DATE'])
data.head(10)

# print(data.head(10))

# cleaning the data
data = data[data.TICKER != 'GEF']

data = data[data.TYPE != 'Intraday']


# remove unwanted columns

drop_cols = ['SPLIT_RATIO', 'EX_DIVIDEND', 'ADJ_FACTOR', 'ADJ_VOLUME', 'ADJ_CLOSE', 'ADJ_LOW', 'ADJ_HIGH', 'ADJ_OPEN', 'VOLUME', 'FREQUENCY', 'TYPE', 'FIGI']
data.drop(drop_cols, axis=1, inplace=True)


print(data)

print("---------------data---------------------")
print(data.OPEN)
print("----------------------------------------")



# Exploratory Data Analysis(EDA)

plt.figure(figsize=(17, 8))
plt.plot(data.CLOSE)
plt.title('Closing price of New Germany Fund Inc (GF)')
plt.ylabel('Closing price ($)')
plt.xlabel('Trading day')
plt.grid(False)
plt.show()


# Moving average filter
# smoothing the time series !


temp_data = data.CLOSE

print("temp_data")
print(temp_data.rolling(window=3).mean())





