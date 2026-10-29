import numpy as np
def spiral_order(x: np.ndarray):
    s=[]
    while min(x.shape[0], x.shape[1])>2:
        for i in range (x.shape[1]):
            s.append(x[0, i])
        for i in range (1, x.shape[0]):
            s.append(x[i, x.shape[1] - 1])
        for i in range (1, x.shape[1]):
            s.append(x[x.shape[0]-1, x.shape[1]-i-1])
        for i in range (1, x.shape[0]-1):
            s.append(x[x.shape[0]-i-1, 0])
    return s
print(spiral_order(np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])))

