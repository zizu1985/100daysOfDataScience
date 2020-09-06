from typing import List, Tuple, Callable
from functools import reduce
import math


# Alias - Lista floatów to vector
Vector = List[float]
Matrix = List[List[float]]

height_weight_age = [70,  # inches
                     170,  # pounds
                     40]  # years

grades = [95,  # exam1
          80,  # exam2
          75,  # exam3
          62]  # exam4


def add(v: Vector, w: Vector) -> Vector:
    """ Add corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def sum_vec(vectors : List[Vector]) -> List[Vector]:
    result = vectors[0]
    for vector in vectors[1:]:
        result = add(result, vector)
    return result


# Using high order function
def sum_red(vectors : List[Vector]) -> List[Vector]:
    return reduce(add,vectors)


def scalar_multiply(v_mult: int, v: Vector) -> Vector:
    return [v_i * v_mult for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, sum_red(vectors))


def dot(v: Vector, w: Vector):
    assert len(v) == len(w), "vectors must be the same length"
    return sum(v_i* w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))


def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A[0] else 0
    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]             # A[i] is already the ith row


def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [A_i[j]          # jth element of row A_i
            for A_i in A]   # for each row A_i


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  #   [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # create one list for each i


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)



if __name__ == "__main__":
    v1 = [1, 2]
    v2 = [2, 3, 4]
    try:
        out = add(v1, v2)
        print(out)
    except Exception as e:
        print("Exception found !")
        print(e)
    v2 = [3, 5]
    print(add(v1,v2))

    # Check adding vectors
    assert add([1, 2], [2, 3]) == [3, 5]

    # Check sum (add more than 2 vectors)
    assert sum_vec([[1,2], [2,3], [3,2]]) == [6, 7]

    assert sum_red([[1, 2], [2, 3], [3, 2]]) == [6, 7]

    print(scalar_multiply(5,[1, 1]))

    assert scalar_multiply(5,[2, 3, 5]) == [10, 15, 25]

    print("End")

    print("Vector Mean")

    assert vector_mean(([1, 2],[3, 4])) == [2, 3]

    print("Checking dot product")
    assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

    print("Checking sum of squares")
    assert sum_of_squares([1, 2, 3]) == 14

    print("Checking magnitude")
    assert magnitude([3, 4]) == 5

    print("Matrixes work")
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[1, 2],
         [3, 4],
         [5, 6]]

    print("Shape of A is %d %d" % (shape(A)[0], shape(A)[1]))
    print("Shape of B is %d %d" % (shape(B)[0], shape(B)[1]))

    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns

    assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 0],
                                  [0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 1]]

    data = [[70, 170, 40],
            [65, 120, 26],
            [77, 250, 19],
            # ....
            ]

    friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

    #            user 0  1  2  3  4  5  6  7  8  9
    #
    friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                     [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                     [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                     [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

    assert friend_matrix[0][2] == 1, "0 and 2 are friends"
    assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

    # only need to look at one row
    friends_of_five = [i
                       for i, is_friend in enumerate(friend_matrix[5])
                       if is_friend]

    print("End")