
'''
This script shows an example of how to index a ndarray with a another boolean ndarray
'''


import numpy as np

if __name__  == '__main__':
    a = np.arange(0, 16).reshape([4,4])

    # The next line will return a 1D array with all the elements in a that are even
    a[(a % 2) == 1]

    # You can also set the value of elements that satisfies some predicate...
    # As an example, all even numbers greater than 7 are replaced by a 0
    a[np.logical_and((a % 2) == 0, a > 7)] = 0

    # You can print again the array after the assignment is done
    # print(a)