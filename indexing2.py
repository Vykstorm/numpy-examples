

'''
This example is the continuation of the example indexing.py.
'''

import numpy as np

if __name__ == '__main__':
    # Indexation using an array as a list of indices
    a = np.arange(0, 10) ** 2

    indices = np.arange(0, 10, 2)
    a[indices], a[indices+1] # this returns the elements at indexes 2i and 2i+1 respectively


    # You can work with multidimensional arrays.
    a = np.array([
        [1, 0, 0],
        [1, 0.5, 0],
        [0.5, 1, 1],
        [0, 0, 0.5]])

    indices = np.array([0, 1, 0])

    # Each value in indices will refer to an index in the most significant dimension of the indexed array.
    # In this case, a file is returned for each index specified, and a 2D array is created using those
    # files concatenated along the most signifcant axis of a
    a[indices]

    # If indices has 2 dimensions for example...
    indices = np.array([
        [0, 1, 0],
        [0, 2, 3]])

    # The resulting array can be seen equivalent as creating a 3D array b where:
    # b[0] = a[indices[0] and b[1] = a[indices[1]]
    b = a[indices]
    assert np.array_equal(b[0], a[indices[0]]) and np.array_equal(b[1], a[indices[1]])

    # Different index arrays can be used for different dimensions
    a = np.arange(0,16).reshape([4,4])
    i = np.array([
        [1,2],
        [2,1]
    ])
    j = np.array([
        [1,2],
        [1,2]
    ])
    a[i,j], a[j,i]