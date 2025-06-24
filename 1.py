import numpy as np

# Sample 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

columns = [arr[:, i].tolist() for i in range(arr.shape[1])]
print(columns)
