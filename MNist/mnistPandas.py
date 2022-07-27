###########################################################
##### Author: Dor Yarchi
# Copyright: © 2022
# Date: 27/07/2022
###########################################################
import pandas as pd
import numpy as np
import os
import shutil

def split7030(df):
    path = "splitted70,30"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

    dfLen = df.shape[0]

    seventy = int(np.floor(0.7 * dfLen))
    thirty = dfLen - seventy

    df70 = df.iloc[:seventy,:]
    df30 = df.iloc[seventy+1:seventy+1+thirty,:]

    df70.to_csv('splitted70,30/70.csv', header=False, index=False)
    df30.to_csv('splitted70,30/30.csv', header=False, index=False)

def seperateByDigit(df):
    path = "splittedByDigit"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

    names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

    for i, digit in enumerate(names):
        oneDigitDf = df[df.iloc[:,-1] == i]

        oneDigitDf.to_csv('splittedByDigit/{}-withLabel.csv'.format(digit), header=False, index=False)
        oneDigitDf.iloc[:,:-1].to_csv('splittedByDigit/{}-withoutLabel.csv'.format(digit), header=False, index=False) 

def halfDigitsMix(df):
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


def Zeros90thers10(df):
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

    """
    # Make sure ratio is ok:
    bambi1 = zerosOthersDf[zerosOthersDf.iloc[:,-1] == 0]
    bambi2 = zerosOthersDf[zerosOthersDf.iloc[:,-1] != 0]

    print(len(bambi1), len(bambi2))



    print("Please choose the name of the CSV to read (without .csv):")
    csvName = input()

    df = pd.read_csv(csvName + '.csv')

    """

    zerosOthersDf.to_csv('zeros90Others10/zerosOthersDf-withLabel.csv', header=False, index=False)
    zerosOthersDf.iloc[:,:-1].to_csv('zeros90Others10/zerosOthersDf-withoutLabel.csv', header=False, index=False)


if __name__ == "__main__":
    print("\nPlease enter the name of the CSV to read (without .csv):")
    csvName = input()

    df = pd.read_csv(csvName + '.csv')
    
    while True:
        print("\n1) Split CSV to 70/30.")
        print("2) Split CSV by digit label.")
        print("3) Split CSV by pairs of digits (50/50).")
        print(r"4) Split CSV to 90% zeros, 10% others.")
        print("\nPlease choose an option:")

        option = input()

        try:
            option = int(option)
        except ValueError:
            print("\nIllegal Input") 
            continue

        if (option > 0 and option <= 4):
            break

        else:
            print("\nIllegal Input") 

    if (option == 1):
        split7030(df)

    elif (option == 2):
         seperateByDigit(df)

    elif (option == 3):
         halfDigitsMix(df)

    elif (option == 4):
         Zeros90thers10(df)