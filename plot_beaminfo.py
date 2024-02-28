import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv("25_incoherent_data.csv")

#df["source_name"].plot(kind = 'hist')
#plt.savefig('Source_name_beam1_bar.png')

df.plot.bar(y='signal_power', x='signal_frequency', rot=0)
plt.savefig('InCoherent_frequency.png')

df.plot(kind = 'scatter', x = 'signal_drift_rate', y='signal_snr')
plt.savefig('scatter_driftrates_incoh.png')
#plot(kind = 'scatter', x = 'signal_frequency', y='signal_snr', c='signal_beam',cmap="tab21)")

#import math as m
#import numpy as np
#import csv
#import matplotlib.pyplot as plt
#import pandas as pd
#import astropy.coordinates as coord
#import astropy.units as u
#from astropy.io import ascii
#from astropy.coordinates import SkyCoord

#xarr2 = np.array(df.iloc[:,22])
#yarr2 = np.array(df.iloc[:,23])
#plt.ylabel('Declination(Radian)')
#plt.xlabel('Right Ascencion (Radian)')
#plt.scatter(xarr2,yarr2)
#plt.savefig('skypositions_beam4.png')

df.plot(kind = 'scatter', x = 'tstart', y='signal_frequency')
plt.savefig('tstart_freq_incoh.png')
