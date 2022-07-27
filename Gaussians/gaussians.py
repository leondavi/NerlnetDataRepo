import numpy as np
import pandas as pd 
import os
import shutil

mu = np.zeros((1,4))
sigma = np.zeros((1,4))

for i in range(4):
    while True:
        print(f"\nPlease enter the mean for gaussian #{i+1}:", end = ' ')
        currentMu = input()

        try:
            mu[0,i] = float(currentMu)
            break

        except ValueError:
            print("\nIllegal Input") 
            continue

    while True:
        print(f"Please enter the std for gaussian #{i+1}:", end = ' ')
        currentSigma = input()

        try:
            sigma[0,i] = float(currentSigma)
            break

        except ValueError:
            print("\nIllegal Input") 
            continue

while True:
    print("\nPlease select the number of rows (samples):", end=' ')
    samples = input()

    try:
        smaples = int(samples)
        break

    except ValueError:
        print("\nIllegal Input") 
        continue

while True:
    print("\nPlease select the number of features:", end=' ')
    features = input()

    try:
        features = int(features)
        break

    except ValueError:
        print("\nIllegal Input") 
        continue

path = "Gaussians CSVs"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

for i in range(4):
    data = np.random.normal(mu[0,i], sigma[0,i], (samples,features))
    labels = np.full((samples,1), mu[0,i])
    dataWithLabels = np.hstack((data, labels))

    df = pd.DataFrame(data = data)
    dfWithLabels = pd.DataFrame(data = dataWithLabels)

    df.to_csv(f'Gaussians CSVs/gaussian{i+1}.csv', header=False, index=False)
    dfWithLabels.to_csv(f'Gaussians CSVs/gaussian{i+1} + Labels.csv', header=False, index=False)






    