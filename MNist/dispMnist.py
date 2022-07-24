import pandas as pd
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt 

df = pd.read_csv('nums_train.csv')

dfArray = df.to_numpy(dtype=np.uint8)

for idx, row in enumerate(dfArray):
    if (row[-1] == 1 or row[-1] == 2 or row[-1] == 8 or row[-1] == 9):
        img = np.reshape(row[:-1], (28,28))
        fig = plt.imshow(img, cmap='gray')
        plt.axis('off')
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.show()

