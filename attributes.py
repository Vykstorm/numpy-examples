

'''
In this example we instantiate a numpy arrray object and show its attributes.
'''

import numpy as np


if __name__ == '__main__':
    '''
    This creates an array 3x3 with the next elements:
    1 2 3
    4 5 6
    7 8 9
    '''
    a = (np.arange(0,9) + 1).reshape([3, 3])

    # Use attribute "ndim" to fetch array dimensions
    print('Number of dimensions: ', a.ndim)

    # Attribute "shape" is a tuple the dimensions of the array
    print('Dims: ', 'x'.join([str(dim) for dim in a.shape]))

    # "size" is the total number of elements
    print('Number of elements: ', a.size)
    assert a.size == np.array(a.shape).prod()

    # "dtype" indicates the underline array element data type.
    # for example: np.uint8, np.uint32, np.float64, ...
    print('Data internal type: ', a.dtype)


    # "itemsize" is the size in bytes used to store each element
    print('Data internal type size: ', '{} bytes'.format(a.itemsize))
    assert a.itemsize == a.dtype.itemsize

    # "buffer" is used as a internal data storage. Points to an object that
    # is responsible of storing array items.
    # a.buffer

    # You can print the array in stdout...
    print(a)