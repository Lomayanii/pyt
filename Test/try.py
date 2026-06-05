import matplotlib.pyplot as plt
import numpy as np

def f(x,t):
    return np.exp(-t)*np.cos(2*np.pi*x*t)

t1 = np.arange(0.0, 5.0, 0.1)

s1 = f(1, t1)
plt.figure()
plt.plot(t1, s1)
plt.show()