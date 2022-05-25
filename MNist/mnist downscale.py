import pandas as pd
import numpy as np
import cv2
import os
import shutil

path = "mnistDownscaled"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

df = pd.read_csv('nums_train.csv')
dfNoLabels = df.iloc[:, :-1] # Drop the labels column

downscaledDf = pd.DataFrame(0, index=np.arange(len(df)), columns=np.arange(257))

print(dfNoLabels.shape)

dfArray = dfNoLabels.to_numpy(dtype=np.uint8) # In order to use cv2 and np on each row, dtype is IMPORTANT

"""
# Example for first row:
img = np.reshape(dfArray[0][:-1], (28,28))
cv2.imshow('Original', img)
cv2.waitKey(0) # Press a key to close window
downscaledImg = cv2.resize(img, (16,16))
cv2.imshow('Downscaled', downscaledImg)
cv2.waitKey(0) # Press a key to close window
"""

for idx, row in enumerate(dfArray):
    img = np.reshape(row, (28,28))
    downscaledImg = cv2.resize(img, (16,16))
    downscaledImgVector = downscaledImg.flatten()
    downscaledDf.iloc[idx,:-1] = downscaledImgVector

"""
# Check if succeded:
bambi = downscaledDf.iloc[0,:-1].to_numpy(dtype=np.uint8)
print(bambi)
bambiImg = np.reshape(bambi, (16,16))
print(bambiImg)
cv2.imshow('Downscaled', bambiImg)
cv2.waitKey(0) # Press a key to close window
"""

downscaledDf.iloc[:,-1] = df.iloc[:,-1] # Add the labels from the original df

downscaledDf.to_csv('mnistDownscaled/mnistDownscaled-labels.csv', header=False, index=False)
downscaledDf.iloc[:,:-1].to_csv('mnistDownscaled/mnistDownscaled-no labels.csv', header=False, index=False)



