import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn
import numpy as np

# ts = pd.Series(pd.read_csv('daily-min-temperatures.csv', header = 0, index_col = 0, squeeze = True))
ts = pd.read_csv('daily-min-temperatures.csv', header = 0, index_col = 0, squeeze = True)
# ts = pd.Series(randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# plt.plot(ts.index, ts.values)
# ts.plot()
# plt.show()
# print(np.mean(ts))

# Z normalization
mean = np.mean(ts)
dev = np.std(ts)
ts_norm = ((ts-mean)/dev)
plt.plot(ts_norm.index, ts_norm.values)
plt.savefig('normalized.png')