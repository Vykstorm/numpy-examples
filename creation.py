


'''
This script shows different ways to create an numpy ndarray object
'''

import numpy as np

if __name__ == '__main__':
    # Create an array from a iterable
    np.array([3,1,4,1,5]) # dtype is guessed from value types
    np.array([3,1,4,1,5], dtype=np.float64) # dtype can be specified as an argument.

    # You can create an array from a previous one with different element type...
    a = np.array([3,1,4,1,5], dtype=np.float64)
    np.array(a, dtype=np.uint8)
    a.astype(dtype=np.uint8)

    # when a list of sublists is specified, the array will have 2 dimensions...
    np.array([[1,0,0], [0,1,0], [0,0,1]])

    # if its a list of sublists of sublits it will have 3, and so on
    np.array([[
                [1,0,0],
                [0,1,0],
                [0,0,1]],
            [
                [0,0,1],
                [0,1,0],
                [1,0,0]
            ]])

    # This array creation syntax is wrong...
    try:
        np.array(1,2,3,4,5)
    except:
        pass

    # You can create your own method to generate a 1D array with that syntax easily...
    def vector(*args):
        return np.array(args)
    assert (vector(1,2,3) == np.array([1,2,3])).all()

    np.zeros([3,3], dtype=np.uint64) # 3x3 array of zeros
    np.ones([3,3], dtype=np.uint64) # 3x3 array of ones
    np.empty([3,3], dtype=np.uint64) # 3x3 array of empty values

    np.arange(0, 20, dtype=np.uint64) # 1D array with all numbers in [0, 20)
    np.arange(1, 20, 2, dtype=np.uint64) # 1D array with eveny numbers in [0, 20)

    # Creates a 1D array with 8 elements equally spaced between the range [0, 7/4 * pi]
    np.linspace(0, 7 / 4 * np.pi, 8) # = ( 0, pi/4, pi/2, 3pi/4, pi, 5pi/4, 3pi/2, 7pi/4)

    # Creates a 3x3 array with random values between [0, 1) using a uniform distribution
    np.random.rand(3, 3)

    # Creates a 3x3 array with random samples of the normal distribution.
    np.random.randn(3,3)

    # Saves an array to a file
    with open('data.csv', 'w') as file:
        np.arange(0, 10, dtype=np.uint64).tofile(file, sep=',')

    # Read array from file
    with open('data.csv', 'r') as file:
        np.fromfile(file, sep=',', dtype=np.uint64)
