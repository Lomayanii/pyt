import numpy as np

# array = np.array([1,2,3,4])
# print(array)
# print(type(array))
# array *= 2
# print(array)

# array2 = np.array([[['A', 34], [4, 345], [234, 345]], [['A', 34], [4, 345], [234, 345]]])
# print(array2.ndim)
# print(array2.shape)
# print(array2[1,1,1] + array2[1,1,1])

#array3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#array[start:end:step]
#print(array3[ ::3])

# array = np.array([1,2,3])
# print(array**5)

# array = np.array([1,2,3])
# print(np.sqrt(array))
# print(np.ceil(array))
# print(np.floor(array))
# print(np.round(array))
# print(np.pi)


# print(np.pi * array **2)


# array1 = np.array([4,5,6,4])
# # print(array1 ** array)

# # #comparison
# # scores = np.array([91,55,100,73,82,64])

# #broadcasting allows numpy to perfom operations between array of different sizes, dimensions need to habe same number or have same size
# array5 = np.array([[1],[2],[3],[4]])
# print(array1 * array5)
# print(array1.shape)
# print(array5.shape)



#aggregate functions
# array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.max(array))
# print(np.min(array))
# print(np.argmin(array))
# print(np.argmax(array))

# print(np.sum(array, axis=0))

# ages = np.array([[21,17,19,16,20,39], [32,56,12,8,15,8]])
# teenagers = ages[ages < 18]

# adults = ages[(ages>=18) & (ages<65)]
# print(teenagers)
# print( adults)
# a2 = np.where(ages>=18, ages, 0)
# print(a2)

# rng = np.random.default_rng(seed=2)
# print(rng.integers(low=1,high=7, size=(3,2)))

#print(np.random.uniform(low=-1, high=1, size=(2,3)))
rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "banana", "orange"])
fruit = rng.choice(fruits, size=(3,3))
print(fruit)
