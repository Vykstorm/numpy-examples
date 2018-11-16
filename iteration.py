
'''
Example that shows how to iterate over the elements of a numpy ndarray
'''

import numpy as np

if __name__ == '__main__':
    # Iterate over the elements in a 1D array
    a = np.arange(0, 16) ** 3
    for item in a:
        pass

    # On arrays with more dimensions, iteration will be done with respect of the first axis.
    a = a.reshape([4,4])
    for row in a:
        pass

    # Finally you can use the flat iterator to iterate over all the element of the array despite its shape.
    for item in a.flat:
        pass