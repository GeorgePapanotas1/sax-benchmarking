import numpy as np
from saxpy.znorm import znorm
from saxpy.paa import paa
from saxpy.sax import ts_to_string
from saxpy.alphabet import cuts_for_asize
import pandas as pd
import string
from sys import getsizeof

def convert_to_sax(dat, word_size, alphabet_size):
    dat_znorm = znorm(dat)
    dat_paa_3 = paa(dat_znorm, word_size)
    sax_string = ts_to_string(dat_paa_3, cuts_for_asize(alphabet_size))
    return sax_string


word_size, alphabet_size = 100, 10

df = pd.read_csv ('first_year_subset.csv')
dat1 = df['Temp'].to_numpy()
sax1 = convert_to_sax(dat1, word_size, alphabet_size)

df = pd.read_csv ('second_year_subset.csv')
dat2 = df['Temp'].to_numpy()
sax2 = convert_to_sax(dat2, word_size, alphabet_size)

print("SAX1: ",sax1)
print("SAX2: ",sax2)

od = np.sqrt(np.sum([(a-b)*(a-b) for a, b in zip(dat1, dat2)]))
print("Original Distance =", od)




def calculateMinDistTable(alpabet_s):
    mindist = np.empty([alpabet_s,alpabet_s])
    breakpoints = cuts_for_asize(alpabet_s)
    for x in range(alpabet_s):
        for y in range(alpabet_s):
            if (abs(x - y) <= 1):
                mindist[x,y] = 0
            else:
                mindist[x,y] = breakpoints[max(x+1,y+1) - 1] - breakpoints[min(x+1,y+1)]
    return mindist

def calculateSaxDistance(sax1, sax2, alph_size):
    alph = string.ascii_lowercase[0:alph_size]
    sax_distance = 0
    mindist = calculateMinDistTable(alph_size)
    for i in range(len(sax1)):
        sax1_index = alph.index(sax1[i])
        sax2_index = alph.index(sax2[i])
        sax_distance = sax_distance + mindist[sax1_index, sax2_index]
    print("SAX Minimum Distance:", sax_distance)
    return sax_distance

    


print("Tighness of Lower bound: ", calculateSaxDistance(sax1, sax2, alphabet_size) / od)
print("SAX word size: ", getsizeof(sax2), " --- Original timeseries size:", dat1.size * dat1.itemsize)

