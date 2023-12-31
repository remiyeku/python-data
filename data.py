# Setup ETL operations?
    # Build e2e data pipeline?
    # ^^^^^^ Download files for years after 2015 in files
    # Join the files 
# Find the average FE (Fuel Economy, MPG) (combined, city, motorway) based on manufacturer
    # Who is top
    # Who is bottom
# Same for emmissions ^
# What is the mean/median distribution of Combined FE
# Does 4WD or 2WD have a higher avg engine power
    # 
# Analyse and compare co2 emissions based on factors (e.g manufacturer)
    # Can look into engine power compared to emissions
    # Can compare Cylinder size to emissions/FE
    # Can look into transmission and emissions/FE (whether autos are more efficient than manuals)
    # Look into FE and co2 emissions
        # Is there a correlation bettween the two

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
df_copy = data.copy()
data.info()

print(df_copy)
#print(data.describe().T)
#print(data.shape)
#print(data.loc[1])
print('------------------')
#print(data.iloc[1])

data_agg = df_copy.agg({"City CO2":['max','min','mean','median','std'], "Combined CO2":['max','min','mean','median','std'], "Engine Displacement":['max','min','mean','median','std']})

print(data_agg.to_string())
print('------------------')

S = np.array([df_copy])

print('------------------')
print(S)
print('------------------')
print(S.shape)
print('------------------')
print(np.ndim(S))
print('------------------')
print(S[0:3, 0:2, 1:3])

# What is the mean/median distribution of Combined FE

FEMean = df_copy.groupby(by=['Carline'])['Combined FE'].mean().sort_values(ascending=False)
FEMedian = df_copy.groupby(by=['Carline'])['Combined FE'].median().sort_values(ascending=False)

plt.subplots(figsize=(10, 8))
plt.plot(FEMean.values, label='mean')
plt.plot(FEMedian.values, label='median')
plt.xlabel('Car Model')
plt.ylabel('Combined FE (MPG)')
plt.title('Mean and Median FE per Car Line')
plt.legend()
plt.show()

# Compute the number of mean/median combined FE over 25mpg

print('Percentage of mean combined FE greater than or equal to 25.0: {}'.format(FEMean[FEMean >= 25.0].shape[0]/FEMean.shape[0]))
print('Percentage of median combined FE greater than or equal to 25.0: {}'.format(FEMedian[FEMedian >= 25.0].shape[0]/FEMedian.shape[0]))


# Find the average FE (Fuel Economy, MPG) (combined, city, motorway) based on manufacturer

FEmanmean = df_copy.groupby(by=['Mfr Name'])['Combined FE'].mean().sort_values(ascending=False)
FEmanmedian = df_copy.groupby(by=['Mfr Name'])['Combined FE'].median().sort_values(ascending=False)

print(FEmanmean)
plt.bar(df_copy.groupby(by=['Mfr Name']), FEmanmedian, color = 'red')
plt.xlabel('Car Manufacturer')
plt.ylabel('Combined FE Avg (MPG)')
plt.title('Mean and Median FE per Car Manufacturer')
plt.legend()
plt.show()
