import numpy as np

def matrix_transpose(A):
    """
    Returns: ndarray, the transpose of A.
    """
    A = np.array(A)
    rows = A.shape[0]
    cols = A.shape[1]

    T = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            T[j][i] = A[i][j]

    return T
