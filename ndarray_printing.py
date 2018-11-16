
'''
This example shows a few ways to print a numpy ndarray
'''

import numpy as np


if __name__ == '__main__':
    # 1D arrays are printed like lists
    print(np.arange(0, 9))
    # 2D arrays are printed as matrices
    print(np.arange(0, 9).reshape([3,3]))

    # To print a 2D array as a flat vector...
    print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(9))
    print(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(9, order='F'))


    # When printing huge arrays, only few items are shown
    print(np.arange(0, 2500).reshape(50, 50))

    # To disable this behaviour, you can do the next:
    # np.set_printoptions(threshold=np.nan)
    print(np.arange(0, 2500).reshape(50, 50))