import numpy as np
import matplotlib.pyplot as plt
from pyts.approximation import PiecewiseAggregateApproximation
import pandas as pd
# Parameters

n_samples, n_timestamps = 10, 48

# Toy dataset
# rng = np.random.RandomState(41)
# X = rng.randn(n_samples, n_timestamps)
# print(X)

X = pd.DataFrame(pd.read_csv('min-temp-subset.csv', header = 2, index_col = 0, squeeze = True, usecols=['Temp']))
#  X= .reshape(-1,1)
print(X)
plt.plot(X)
plt.show()
# PAA transformation
window_size = 10.5
paa = PiecewiseAggregateApproximation(window_size=window_size)
X_paa = paa.transform(X)

# Show the results for the first time series
plt.figure(figsize=(6, 4))
plt.plot(X[0], 'o--', ms=4, label='Original')
plt.plot(np.arange(window_size // 2,
                   n_timestamps + window_size // 2,
                   window_size), X_paa[0], 'o--', ms=4, label='PAA')
plt.vlines(np.arange(0, n_timestamps, window_size) - 0.5,
           X[0].min(), X[0].max(), color='g', linestyles='--', linewidth=0.5)
plt.legend(loc='best', fontsize=10)
plt.xlabel('Time', fontsize=12)
plt.title('Piecewise Aggregate Approximation', fontsize=16)
plt.show()
