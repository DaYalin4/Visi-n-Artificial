import numpy as np
import matplotlib.pyplot as plt


#imagen negra
img = np.zeros((10,10, 1), np.uint8)


img[2,1,0] = 20
img[2,3,0] = 50
img[2,5,0] = 100
img[2,7,0] = 125
img[2,9,0] = 255


print(img[:,:,0])


plt.imshow(img, cmap="gray")

plt.show()
