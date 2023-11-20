import pandas as pd

data = pd.read_csv('data.csv')
db_copy = data.copy()

print(data)
#print(data.describe().T)
#print(data.shape)
#print(data.loc[1])
print('------------------')
#print(data.iloc[1])

data_agg = db_copy.agg({"City CO2":['max','min','mean','median','std'], "Combined CO2":['max','min','mean','median','std'], "Engine Displacement":['max','min','mean','median','std']})

print(data_agg.to_string())