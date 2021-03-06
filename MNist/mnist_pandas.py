import pandas as pd
import numpy as np
import os
import shutil

df = pd.read_csv('nums_train.csv')

"""
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

"""
# Task 2 - Pairs of 50-50 digits:
path = "pairsOfDigits"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

names = ['Zero+One','One+Two','Two+Three','Three+Four','Four+Five', \
        'Five+Six','Six+Seven','Seven+Eight','Eight+Nine']

for i, name in enumerate(names):
    digit1Df = df[df.iloc[:,-1] == i]
    digit2Df = df[df.iloc[:,-1] == i+1]

    pairDf = pd.concat([digit1Df.head(3795),digit2Df.head(3795)]) # 3795 is the min. number of rows for a digit
    pairDf = pairDf.sample(frac=1) # Shuffle the rows

    pairDf.to_csv('pairsOfDigits/{}-withLabel.csv'.format(name), header=False, index=False)
    pairDf.iloc[:,:-1].to_csv('pairsOfDigits/{}-withoutLabel.csv'.format(name), header=False, index=False) 

"""
# Task 3 - 90% zeros, 10% others:
path = "zeros90Others10"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

zerosDf = df[df.iloc[:,-1] == 0]
othersDf = df[df.iloc[:,-1] != 0]

# Make sure no. of rows in zeros df is divisble by 9:
while (len(zerosDf) % 9 != 0):
    zerosDf = zerosDf.iloc[:-1][:]

n = len(zerosDf)

zerosOthersDf = pd.concat([zerosDf,othersDf.head(int(n/9))]) 
zerosOthersDf = zerosOthersDf.sample(frac=1) # Shuffle the rows


# Make sure ratio is ok:
bambi1 = zerosOthersDf[zerosOthersDf.iloc[:,-1] == 0]
bambi2 = zerosOthersDf[zerosOthersDf.iloc[:,-1] != 0]

print(len(bambi1), len(bambi2))


zerosOthersDf.to_csv('zeros90Others10/zerosOthersDf-withLabel.csv', header=False, index=False)
zerosOthersDf.iloc[:,:-1].to_csv('zeros90Others10/zerosOthersDf-withoutLabel.csv', header=False, index=False)
"""