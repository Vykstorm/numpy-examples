

'''
Example showing how to manipulate the shape of an array
'''


import numpy as np


if __name__ == '__main__':
    # The next methods doesnt change the array data, but only its shape.
    a = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]])

    # Turns array into 1D
    a.flatten()

    # Changes the array into a modified shape
    a.reshape([2,8])

    # Returns the tranposed matrix
    a.transpose()
    a.T.reshape([2,8])
    a.reshape([2,8]).T

    # reshape() returns a new version of the array with the shape modified.
    # resize() method changes the shape of the array itself
    a = np.arange(0, 10)
    a.resize([3,3])
    assert a.shape == (3,3)