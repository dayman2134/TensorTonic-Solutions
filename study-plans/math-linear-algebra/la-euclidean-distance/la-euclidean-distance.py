import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x = np.array(x)
    y = np.array(y)
    diff = x-y
    return np.sqrt(np.sum(diff*diff))
    