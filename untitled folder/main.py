import numpy as np
import matplotlib as plt
from pandas import read_csv

series = read_csv('daily-min-temperatures.csv', header=0, index_col=0)
# values = series.values
# print(values)
# values = values.reshape((len(values), 1))
# print(values)
series = Series(series)

series.plot()
# a = np.array([-1,2,3,4,1,2,3,4,5])
# print(np.std(a))