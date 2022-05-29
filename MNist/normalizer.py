import pandas as pd
import numpy as np
from sklearn import preprocessing
import os
import shutil

path = "dgfdfgdfgdfg"
if os.path.exists(path):
    while True:
        print("Folder already exists.\n")
        print(r"Would you liek to delete it and create a new one instead [y\n]?")
        choice = input()
        if choice == 'y':
            shutil.rmtree(path)
        elif choice == 'n':
            print('Aborted.')
        else:
            print('Wrong input.')
            continue
os.mkdir(path)

df = pd.read_csv('nums_train.csv')

x = df.values # Returns a numpy array

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)

dfNormalized = pd.DataFrame(x_scaled)

dfNormalized.to_csv(path + '/dfNormalized-withLabels.csv', header=False, index=False)
dfNormalized.iloc[:,:-1].to_csv(path + '/dfNormalized-noLabels.csv', header=False, index=False)