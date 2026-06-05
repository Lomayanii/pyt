import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img2 = cv.imread("C:/pyt/Learning/testp.jpg")
img3 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)


def max_pooling(img):
    i,j = 0, 0
    h, w = img.shape[:2]
    pooled = np.zeros(((int)(h/2.0),(int)(w/2.0)), dtype=np.uint8)
    while(i<(int)(h/2.0)):
        while(j<(int)(w/2.0)):
            temp = np.max(img[(i*2):(i*2+2), (j*2):(j*2+2)])
           
            pooled[i, j] = temp
            j = j+1

        i = i+1
        j = 0
        
    return pooled    

#pool = max_pooling(img2)

def max_pooling_2(img, k):
    b, g, r = cv.split(img)
    i,j = 0, 0
    h, w = img.shape[:2]
    pooledb = np.zeros((h//k, w//k), dtype = np.uint8)
    pooledg = np.zeros((h//k, w//k), dtype = np.uint8)
    pooledr = np.zeros((h//k, w//k), dtype = np.uint8)
    while(i < h//k):
        while(j < w//k):
            pooledb[i,j] = np.max(b[(i*k):(i*k+k), (j*k):(j*k+k)])
            pooledg[i,j] = np.max(g[(i*k):(i*k+k), (j*k):(j*k+k)])
            pooledr[i,j] = np.max(r[(i*k):(i*k+k), (j*k):(j*k+k)])
            j=j+1
        i=i+1
        j=0
    return cv.merge([pooledr, pooledg, pooledb])

# pool = max_pooling_2(img2,10)
# plt.imshow(pool)
# plt.show()


def patternmatch(img, pattern):
    i, j = 0, 0
    h, w = img.shape[:2]
    h_p, w_p = pattern.shape[:2]
    padded = np.zeros((h + h_p - 1, w + w_p - 1), dtype=np.uint8)
    
    while(i < h):
        while(j < w):
            padded[i + h_p//2, j +  w_p//2] = img[i, j]
            j = j + 1
        i = i + 1
        j = 0
    
    i, j, m, s = 0, 0 , 0, 0
    zustand = 0
    stop = False
    ausgabe = np.zeros((h, w), dtype=np.uint8)
    while(i < h ):
        while(j < w ):
            for k in range(h_p): 
                for l in range(w_p):
                    if(padded[(i )+k, (j )+l] == pattern[k,l]):
                        zustand = 1
                    else: 
                        zustand = 0
                        stop = True
                        break
                if stop: 
                    break
            if(zustand == 1):
                ausgabe[m,s] = 1
            else:
                ausgabe[m,s] = 0
            j = j + 1 
            s = s + 1
            stop = False
            zustand = 0
        j = 0
        s = 0
        i = i + 1
        m = m + 1
    return ausgabe



pattern = np.array([[1,1,1],
                    [1,1,1],
                    [1,1,1]])

# match = patternmatch(img3, pattern)

# plt.imshow(match, cmap="gray")
# plt.show()


def pattern_match_2(img, pattern):
    h, w = img.shape
    h_p, w_p = pattern.shape
    
    pad_y = h_p //2
    pad_x = w_p//2
    
    padded = np.zeros((h +h_p, w + w_p), dtype = img.dtype)
    padded[pad_y:pad_y+h, pad_x:pad_x+w] = img
    
    out = np.zeros((h, w), dtype=img.dtype)
    
    for i in range(h):
        for j in range(w):
            window = padded[i:i+h_p, j:j+w_p]
            if np.array_equal(window, pattern):
                out[i, j] = 1
    return out

match2 = pattern_match_2(img3, pattern)

plt.imshow(match2, cmap="gray")
plt.show()

