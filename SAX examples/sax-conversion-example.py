import numpy as np
from saxpy.znorm import znorm
from saxpy.paa import paa
from saxpy.sax import ts_to_string
from saxpy.alphabet import cuts_for_asize
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv ('first_year_subset.csv')
word_size, alphabet_size = 12, 3

dat = df['Temp'].to_numpy()

fig, ax = plt.subplots()
ax.plot(dat)
ax.set(xlabel='Days Index', ylabel='Minimum Temperature (°C)',title='Original Timeseries - Minimum Daily Temperatures')
ax.grid()
fig.savefig("normal.png")
plt.show()


dat_znorm = znorm(dat)

fig, ax = plt.subplots()
ax.plot(dat_znorm)
ax.set(xlabel='Days Index', ylabel='Minimum Temperature (°C)',title='Original Timeseries - Z-normalized')
ax.grid()
fig.savefig("z-norm.png")
plt.show()

dat_paa_3 = paa(dat_znorm, word_size)

fig, ax = plt.subplots()
ax.plot(dat_paa_3, 'o-')
ax.set(xlabel='Days Index', ylabel='Minimum Temperature (°C)',title='Piecewise Aggregate Approximation ')
ax.grid()
fig.savefig("paa.png")
plt.show()


sax_string = ts_to_string(dat_paa_3, cuts_for_asize(alphabet_size))

fig, ax = plt.subplots()
ax.plot(dat_paa_3, 'o-')
ax.set(xlabel='Days Index', ylabel='Minimum Temperature (°C)',title='Symbolic Aggregate approXimation')
plt.hlines(cuts_for_asize(alphabet_size), 0, word_size, color='g', linestyles='--', linewidth=0.5)
for i in range(len(dat_paa_3)):
    plt.text(i, dat_paa_3[i], sax_string[i], ha='center', va='bottom', fontsize=14, color='#ff7f0e')


fig.savefig("sax.png")
plt.show()
print("Final SAX Result: ", sax_string)

