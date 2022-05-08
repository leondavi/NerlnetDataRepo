import pandas as pd
import numpy as np

# Import data
df = pd.read_csv('HeartTrain.csv')

print(df.shape)

df.replace('', np.nan, inplace=True)
df.dropna(inplace=True)

print(df.shape)

df.to_csv('HeartTrainBlankDropped.csv')