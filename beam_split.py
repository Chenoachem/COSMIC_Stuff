import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df=pd.read_csv("25_coherent_data.csv")

beam0=df.loc[df.signal_beam==0]
beam1=df.loc[df.signal_beam==1]
beam2=df.loc[df.signal_beam==2]
beam3=df.loc[df.signal_beam==3]
beam4=df.loc[df.signal_beam==4]

beam0.to_pickle('beam0_25GHz_highter.pkl')
beam1.to_pickle('beam1_25GHz_highter.pkl')
beam2.to_pickle('beam2_25GHz_highter.pkl')
beam3.to_pickle('beam3_25GHz_highter.pkl')
beam4.to_pickle('beam4_25GHz_highter.pkl')
