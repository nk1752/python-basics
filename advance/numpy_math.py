import numpy as np

def np_size(a, b, c) -> int:
    a = np.arange(a).reshape(b, c)
    return a.size