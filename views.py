
'''
This example shows the basic properties of an array view in numpy
'''

import numpy as np


if __name__ == '__main__':
    a = np.arange(0, 10, 2)

    # You can create a view of an existing array using the method view()
    b = a.view()
    assert a.shape == b.shape
    assert a is not b
    assert not b.flags.owndata and b.base is a

    # Any change to the view is reflected also in the underline array
    b += 1
    assert (a == b).all()
    b -= 1

    # Any slice of the array obtained via indexation is also a view.
    b = a[2:-1]
    assert a is not b
    assert not b.flags.owndata and b.base is a

    b += 1
    assert (b == a[2:-1]).all()
    b -= 1


    # You can call copy() to retrieve a deep copy of an arbitrary array. Either the object and data will be
    # independent

    b = a.copy()
    assert a is not b
    assert b.flags.owndata and b.base is not a

    b += 1
    assert (b != a).all()