
'''
Example showing how to stack multiple arrays into one.
'''

import numpy as np

if __name__ == '__main__':
    # Stacking 1D arrays as rows to compose a 2D array
    a, b = np.arange(0, 6, dtype=np.uint8), np.arange(6, 12, dtype=np.uint8)
    np.vstack([a,b])
    np.row_stack([a,b])

    # Stacking 1D arrays as columns to create a 2D array
    np.hstack([a,b])
    np.column_stack([a,b])

    # Stacking 2D arrays by rows
    a.resize([2,3])
    b.resize([2,3])

    np.vstack([a,b])
    np.row_stack([a,b])
    np.concatenate([a,b], axis=0)

    # Stacking 2D arrays by columns
    np.hstack([a,b])
    np.column_stack([a,b])
    np.concatenate([a,b], axis=1)

    # Also you can repeat an array along some dimension
    # using the method repeat() instead of vstack, hstack, ...
    a = np.array([
        [1, 0],
        [0, 1]])
    np.vstack([a,a])
    np.repeat(a, 2, axis=0)
    np.repeat(a, 4, axis=1)