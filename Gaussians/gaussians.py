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
        samples = int(samples)
        break

    except ValueError:
        print("\nIllegal Input") 
        continue

while True:
    print("Please select the number of columns (features):", end=' ')
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

data = np.zeros((1,4,samples,features))
labeledData = np.zeros((1,4,samples,features+1))

for i in range(4):
    data[0,i,:,:] = np.random.normal(mu[0,i], sigma[0,i], (samples,features))
    labels = np.full((samples,1), mu[0,i]) # MU (MEAN) IS THE LABEL!! NOT THE GAUSSIAN NUMBER!
    labeledData[0,i,:,:] = np.hstack((data[0,i,:,:], labels))

    df = pd.DataFrame(data = data[0,i,:,:])
    dfWithLabels = pd.DataFrame(data = labeledData[0,i,:,:])

    df.to_csv(f'Gaussians CSVs/gaussian{i+1}_predict.csv', header=False, index=False)
    dfWithLabels.to_csv(f'Gaussians CSVs/gaussian{i+1}_train.csv', header=False, index=False)

for i in range(0,3,2):
    gauss1 = pd.DataFrame(data = data[0,i,:,:])
    gauss2 = pd.DataFrame(data = data[0,i+1,:,:])
    mixData = pd.concat([gauss1, gauss2])
    mixData = mixData.sample(frac=1).reset_index(drop=True)

    labledGauss1 = pd.DataFrame(data = labeledData[0,i,:,:])
    labledGauss2 = pd.DataFrame(data = labeledData[0,i+1,:,:])
    labledMixData = pd.concat([labledGauss1, labledGauss2])
    labledMixData = labledMixData.sample(frac=1).reset_index(drop=True)

    mixData.to_csv(f'Gaussians CSVs/mix{i+1}and{i+2}_predict.csv', header=False, index=False)
    labledMixData.to_csv(f'Gaussians CSVs/mix{i+1}and{i+2}_train.csv', header=False, index=False)

allGaussMix = pd.concat([pd.DataFrame(data = data[0,0,:,:]),\
    pd.DataFrame(data = data[0,1,:,:]),\
    pd.DataFrame(data = data[0,2,:,:]),\
    pd.DataFrame(data = data[0,3,:,:])])

allGaussMix = allGaussMix.sample(frac=1).reset_index(drop=True)

labeldAllGaussMix = pd.concat([pd.DataFrame(data = labeledData[0,0,:,:]),\
    pd.DataFrame(data = labeledData[0,1,:,:]),\
    pd.DataFrame(data = labeledData[0,2,:,:]),\
    pd.DataFrame(data = labeledData[0,3,:,:])])

labeldAllGaussMix = labeldAllGaussMix.sample(frac=1).reset_index(drop=True)   

allGaussMix.to_csv(f'Gaussians CSVs/mixAllGaussian_predict.csv', header=False, index=False)
labeldAllGaussMix.to_csv(f'Gaussians CSVs/mixAllGaussian_train.csv', header=False, index=False)




    