# numpy-examples
Very basic usage examples of numpy python library, following the quickstart tutorial of SciPy in its docs:
https://docs.scipy.org/doc/numpy-1.15.1/user/quickstart.html

All examples provided are avaliable at the root of this repository.
This is a piece of code of the example creation.py:

```python
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
```
