import pandas as pd
import numpy as np
import os
import shutil

df = pd.read_csv('nums_train.csv')



# Task 1 - Seperate CSVs for each digit:
path = "splittedByDigit"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

for i, digit in enumerate(names):
    oneDigitDf = df[df.iloc[:,-1] == i]

    oneDigitDf.to_csv('splittedByDigit/{}-withLabel.csv'.format(digit), header=False, index=False)
    oneDigitDf.iloc[:,:-1].to_csv('splittedByDigit/{}-withoutLabel.csv'.format(digit), header=False, index=False) 