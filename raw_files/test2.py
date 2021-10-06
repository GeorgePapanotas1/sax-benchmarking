import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn
import numpy as np

# ts = pd.Series(pd.read_csv('daily-min-temperatures.csv', header = 0, index_col = 0, squeeze = True))
# ts = pd.read_csv('daily-min-temperatures.csv', header = 0, index_col = 0, squeeze = True)
# ts = pd.Series(randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()

ts = pd.Series([2.02, 2.33, 2.99, 6.85, 9.20, 8.80, 7.50, 6.00, 5.85, 3.85, 4.85, 3.85, 2.22, 1.45, 1.34])

mean = np.mean(ts)
dev = np.std(ts)
ts_norm = ((ts-mean)/dev)
print(ts)
print(ts_norm.mean(axis=0))

# def paa(ts, paa_size):
#     length = len(ts)
#     if length == paa_size:
#         return ts
#     else: 
#         if length % paa_size == 0: 
