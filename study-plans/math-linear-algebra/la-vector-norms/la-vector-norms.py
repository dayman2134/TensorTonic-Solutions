import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.array(v)
    l1 = np.sum(np.abs(v))
    l2 = np.sqrt(np.sum(v * v))
    linf = np.max(np.abs(v))

    return np.array([l1, l2, linf], dtype=np.float64)
    