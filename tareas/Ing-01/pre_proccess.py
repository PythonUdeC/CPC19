
import pandas as pd
import sys
import numpy as np

df = pd.read_csv('./sun_raw.csv')
df['Latitude'] = df['the_geom_4326'].str.split().str.get(0)
df['Longitude'] = df['the_geom_4326'].str.split().str.get(1)
df.to_csv('sun.csv')

