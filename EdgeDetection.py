import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images.JPG', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.array([
            [1,-1], 
            [1,-1],            
        ])
edge_img = cv2.filter2D(img, -1, kernel)

f, axes = plt.subplots(1,2, figsize=(20,10))
axes[0].imshow(img)
axes[0].set_title('origin')
axes[1].imshow(edge_img)
axes[1].set_title('result')
plt.show()
