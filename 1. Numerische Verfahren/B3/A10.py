import numpy as np

# eps = np.finfo(float).eps
# print(eps)
# print((-1+1)+eps/2)
# print(-1 + (1+eps/2))

n = 5000000


print(np.sum(1.0/np.arange(1, n + 1, dtype=np.float32)))
