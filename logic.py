

'''
This example shows a few logic functions to maniuplate numpy ndarrays
For a complete list of logic methods, you can check the docs:
https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.logic.html
'''

import numpy as np


if __name__ == '__main__':
    a = np.arange(0, 20, 2, dtype=np.float64)
    b = np.arange(0, 20, 2, dtype=np.uint8)

    # Check for equality/inequality of element in an array (element-wise)
    a == b, a != b
    np.equal(a, b), np.not_equal(a, b)

    np.array_equal(a, b) # This ensures that both the shape and the elements of the arrays are the same (not element-wise)

    a = np.array([
        [1, 0],
        [1, 0]], dtype=np.float64)
    b = np.array([1, 0], dtype=np.float64)

    # array_equiv() method check if both the shape and the items are equal as method array_equal()
    np.array_equiv(a, a.astype(dtype=np.uint8))

    # if the shape is not equal, it checks if one of the arrays can be broadcasted to fit the shape of the other array...
    np.array_equiv(b, a)

    # Few comparision methods (element-wise) are also avaliable...
    a, b = np.arange(0,10,2), np.arange(1,11, 2)
    a > b, a < b, a >= b, a <= b

    # To create a predicate of the style: "if all elements satisifies a condition", you can use method all()
    # all() returns True if all elements in an array are evaluated to True. When array dtype is bool this is true when all
    # element have value True.
    a = np.arange(0, 10)
    b = a + 1
    (a > b).all(), (a >= b).all()

    # On the other hand, any() method returns True if at least 1 element is evaluated to True.
    a = np.random.rand(5)
    (a >= 0.5).any()

    # You can create more complex predicates using unary and binary logical operations (not, and, or, xor)
    # Such operations are element-wise when both operands are arrays.
    a, b = np.random.rand(5), np.random.rand(5)
    np.logical_xor((a >= 0.5), (b < 0.5))
    np.logical_and((a >= 0.5), (b >= 0.5))


    # If you have an array and you want to check if the absolute difference between its values and some arbitrary value
    # is close to some threshold...
    threshold = 0.5
    a = np.arange(0, 10, 2)
    b = a + np.random.rand(5)
    np.isclose(a, b, atol=threshold,rtol=0)

    # np.allclose(...) is equivalent to np.isclose(...).all()
    a = np.arange(0, 10, 2)
    b = a + 0.45
    np.allclose(a, b, atol=0.5,rtol=0)
