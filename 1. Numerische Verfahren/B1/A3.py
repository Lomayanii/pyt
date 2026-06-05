import numpy as np

a = np.linspace (0, 5, 5, dtype=float)
#print(a)
u = np.array([0, 5, -4], dtype=float)
v = np.array([0.2, 3, 6], dtype=float)
A = np.array([[1,2,3],[0,8,7]], dtype=float)
# print(np.inner(u, v))
# print(np.linalg.norm(u))
# print(np.cross(u, v))
# print(np.dot(u,v))
# print(A)
# print(np.dot(A,u))

# print(u*v) #Komponentenweise Multiplikation
# print(A*A)
# print(len(u))
# print(A.shape)
# print(A[0:2, 1:3])

# A[1,:] = A[1,:]+A[0,:]
# print(A[1,:])

# B = A
# A[0,0]= 4.6
# print(B)
# B = A.copy()
# A[0,0] = 9
# print(B)

#help(np.eye)
M = 2 * np.eye(3,3) - np.eye(3,3,1) - np.eye(3,3,-1)


# help(np.linalg.solve)
x = np.linalg.solve(M,u)
print(x)

help(np.zeros_like)