import numpy as np
import scipy.linalg as la
from typing import List

Vector = List[float]


def add(v: np.array, w: np.array) -> np.array:
    """ Add corresponding elements"""
    assert v.shape == w.shape, "1D numpy array shape should be equal"
    return v + w


if __name__ == "__main__":
    print("Begin")
    np.testing.assert_array_equal(add(np.array([1, 2]), np.array([3, 4])), np.array([4, 6]), "Numpy adding arrays doesn't work")
    print("End")
