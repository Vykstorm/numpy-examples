

'''
Just like the previous example which shows how to stack multiple ndarrays togethers, this one demonstrates how
to split an array into different parts.
'''

import numpy as np


if __name__ == '__main__':
    # Split a 2D array horizontally
    a = np.arange(0, 16).reshape([4,4])

    np.hsplit(a, 4), np.hsplit(a, 2)
    np.array_split(a, 4, axis=0), np.array_split(a, 2, axis=0)

    # Split a 2D array vertically
    np.vsplit(a, 4), np.vsplit(a, 2)
    np.array_split(a, 4, axis=1), np.array_split(a, 2, axis=1)
