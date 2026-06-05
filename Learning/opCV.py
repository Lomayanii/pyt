import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("C:/pyt/Learning/testp.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img)
print(img.shape)
print(gray.shape)
print(img.dtype)

value = gray[0,0]
gray[0,0] = 255

dst = gray.copy()
dst = np.clip(gray.astype(np.float32)*0.1,0,255).astype(np.uint8)

kernel = np.array([
    [1,2,1],
    [2,4,2],
    [1,2,1]
], dtype=np.float32) / 16.0
smoothed = cv.filter2D(gray.astype(np.float32), -1, kernel)

sobel_x = np.array([
    [1,0,-1],
    [2,0,-2],
    [1,0,-1]
], dtype=np.float32)

sobel_y = sobel_x.T

dx = cv.filter2D(gray.astype(np.float32), -1, sobel_x)
dy= cv.filter2D(gray.astype(np.float32), -1, sobel_y)
mag = np.sqrt(dx**2 + dy**2)

#plt.imshow(gray, cmap="gray")
plt.imshow(gray)
#plt.axis("off")
plt.show()