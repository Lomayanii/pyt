import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def graustufen(img):
    h, w = img.shape[:2]
    out = np.zeros((h, w), dtype=np.uint8)
    
    b, g, r = cv.split(img)
    for i in range(h):
        for j in range(w):
            out[i,j] =  np.round((0.2 * r[i, j] + 0.7 * g[i, j] + 0.1 * b[i, j]))
            
    return out
           
img = cv.imread("C:/pyt/Learning/testp.jpg")

grey = graustufen(img)
# plt.imshow(grey, cmap="gray")
# plt.show()

def grau_rahmen(img, radius):
    i, j = 0, 0 
    h, w = img.shape[:2]
    mid_y, mid_x = h//2, w//2
    b, g, r = cv.split(img)

    outb = np.zeros((h, w), dtype=np.uint8)
    outg = np.zeros((h, w), dtype=np.uint8)
    outr = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if((i - mid_y)**2 + (j - mid_x)**2 > radius**2):
                    outb[i, j] =  np.round((0.2 * r[i, j] + 0.7 * g[i, j] + 0.1 * b[i, j]))
                    outg[i, j] =  np.round((0.2 * r[i, j] + 0.7 * g[i, j] + 0.1 * b[i, j]))
                    outr[i, j] =  np.round((0.2 * r[i, j] + 0.7 * g[i, j] + 0.1 * b[i, j]))
            else: 
                    outb[i, j] = b[i, j]
                    outg[i, j] = g[i, j]
                    outr[i, j] = r[i, j]
            
    return cv.merge([outb, outg, outr])
           
#circle = grau_rahmen(img, 500)
# plt.imshow(cv.cvtColor(circle, cv.COLOR_BGR2RGB))
# plt.show()
            
            
def histogramm(img, num_bins):
    h, w = img.shape[:2]
    bins = np.zeros(num_bins, dtype=int)
   
    
    abstand = 256 // num_bins
   
    for i in range(h):
        for j in range(w):
            for k in range(num_bins):
                if abstand * k <= img[i, j] < abstand * (k + 1):
                    bins[k] +=1
                    break
                    
    return bins
    
h = histogramm(grey, 4)
x = np.arange(4)
plt.bar(x, h)

plt.show()
