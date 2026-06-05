import numpy as np

d = 1e-12
A = np.array([[1,1], [0,d]])
print(A)

print(np.linalg.cond(A, 2))
