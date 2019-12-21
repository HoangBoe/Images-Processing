import cv2
import numpy as np
import matplotlib.pyplot as plt

gray_im = cv2.imread('objects1.jpg', 1)
gray_im = cv2.cvtColor(gray_im, cv2.COLOR_BGR2GRAY)
gray_correct = np.array(255 * (gray_im / 255) ** 1.2 , dtype='uint8')
plt.subplot(222)
plt.title('Gamma Correction y= 1.2')
plt.imshow(gray_correct, cmap="gray", vmin=0, vmax=255)