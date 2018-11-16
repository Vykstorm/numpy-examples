


'''
This script shows a few numpy ndarrays basic operations

A complete list of universal functions (ufuncs) of numpy are presented here:
https://docs.scipy.org/doc/numpy-1.13.0/reference/ufuncs.html
'''

import numpy as np
import sys


if __name__ == '__main__':
    arange = lambda *args: np.arange(*args, dtype=np.int64)
    ones = lambda shape: np.ones(shape, dtype=np.int64)
    zeros = lambda shape: np.zeros(shape, dtype=np.int64)

    # Basic arithmetic operations (element-wise)
    arange(0, 10) + ones([10])
    arange(0, 10) + 1
    arange(0, 10, 2) * arange(1, 11, 2)
    arange(0, 10) ** 2

    # Matrix products can be computed using dot() or operator @ in python >= 3.5
    a = np.array([
        [1, 0],
        [0, 1]])
    b = np.array([
        [2, 2],
        [2, 2]])
    # Element-wise product
    a * b

    # Normal matrix multiplication
    a.dot(b)
    if sys.version_info >= (3,5):
        a @ b
        assert (a.dot(b) == a @ b).all()

    '''
    Arithmetic operations returns new created matrices with their results in it. You can self-assign the results
    to one of the operands
    '''
    a = np.array([
        [1,0],
        [0,1]])
    a *= 2
    a += 1


    # There exists ndarray bounded methods for few unary operations such as min(), max(), mean(), ...
    a = np.arange(0, 9).reshape([3, 3])
    a.min()
    a.max(axis = 1)
    a.cumsum(axis = 1)
    a.mean(axis = 0)


    # numpy provides a set of universal functions (ufunc), like sin(), cos(), exp(), ...
    a = np.linspace(0, 7 / 4 * np.pi, 8) # = ( 0, pi/4, pi/2, 3pi/4, pi, 5pi/4, 3pi/2, 7pi/4)
    np.sin(a) ** 2 + np.cos(a) ** 2
    np.sqrt(np.arange(1, 12, 2).cumsum())
    np.floor(np.random.rand(10) * 2).astype(np.int8)
    np.sign(np.random.rand(10) - 0.5).astype(np.int8)

