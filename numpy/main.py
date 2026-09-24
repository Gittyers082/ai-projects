import numpy as np

arr_1d = np.array([10, 20, 30, 40])
print(arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid.shape)  
print(grid.ndim)   
print(grid.size)  

prices = np.array([10, 20, 30])
print(prices * 2)  

fees = np.array([1, 2, 3])
print(prices + fees)  

data = np.array([10, 20, 30, 40, 50])
print(data[0])     
print(data[1:4])  

matrix = np.array([[10, 20, 30], [40, 50, 60]])
print(matrix[1, 1])  
print(matrix[0, :])  
