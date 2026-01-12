import pandas as pd
import ppigrf
import numpy as np

df = pd.read_csv('data.csv', sep=None, engine='python')

def hitung(row):
    Be, Bn, Bu = ppigrf.igrf(row['Longitude'], row['Latitude'], row['Elevasi']/1000, pd.to_datetime(row['Tanggal'], dayfirst=True))
    
    Be, Bn, Bu = Be[0], Bn[0], Bu[0]
    
    H = np.sqrt(Bn**2 + Be**2)
    F = np.sqrt(H**2 + Bu**2)
    Dec = np.degrees(np.arctan2(Be, Bn))
    Inc = np.degrees(np.arctan2(-Bu, H))

    return pd.Series([F, Dec, Inc])

df[['IGRF_F', 'IGRF_Dec', 'IGRF_Inc']] = df.apply(hitung, axis=1)
df.to_csv('hasil_igrf.csv', index=False)